import socket
import threading
import sys
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
from Final_plot import plot_histogram, plot_data
from config import *

# Definir el host y puerto del servidor

init = True
activate_thread = True
plot = False
flag = False
counter = 0
maximos = []

# Definir una lista para almacenar los datos recibidos
ys = [0]*GRAPH_LENGTH
flags = [0]*GRAPH_LENGTH # 0 = no video, 1 = video


wenas = [ys]
wenascolor = ['#f000ff']
data_user = []
flags_user = []
flagwena = 0
flag1 = True
flag2 = False


def actualize_list(data):
    global wenas
    global wenascolor
    global flag
    global flag1
    global flag2

    
    if flag and flag1:
        wenas.append([])
        wenascolor.append('#20FF16')
        flag1 = False
        flag2 = True

    elif not(flag) and flag2:
        wenas.append([])
        wenascolor.append('#f000ff')
        flag1 = True
        flag2 = False

    
    
    # pop the fist element of the first list in wenas
    wenas[0].pop(0)
    # append the new data to the last list in wenas
    wenas[-1].append(data)

    # pop first item if has an empty list
    if len(wenas[0]) == 0:
        wenas.pop(0)
        wenascolor.pop(0)

    data_user.append(data)
    flags_user.append(1 if flag else 0)

def send_activate(sock):
    sock.sendall("test".encode())

def receive_data(sock):
    global activate_thread
    global plot
    global counter
    global maximos
    global flag


    while True:
        # Recibir datos desde el servidor
        data = sock.recv(1024).decode()

        if not data:
            break


        if (activate_thread):
            print("entro")
            plot = True
            activate_thread = False

        if "nueva" in data:
            counter += 1
            print(f"Repetición número {counter}")
            
            # data is a string separated by commas
            ang = data.split(",")[1]
            print(ang)
            maximos.append(float(ang))
            flag = False


        elif "entrar" in data:
            print("Se puso video")
            flag = True

        
        else:
            
            # try to convert data to float. If it fails, just ignore it
            
            try:
                data_float = float(data[0:5])
            except:
                continue

            actualize_list(data_float)




# function to update the data
def my_function(i):

    # clear axis
    ax.cla()

    # time vector
    time = [i*0.02 for i in range(GRAPH_LENGTH)]

    # color of the last point
    actual_color = '#1AB804' if flag else '#FF0D8A'
    ax.set(
        title=f"[ repetición: {counter} ]",
        xlabel="Tiempo (s)",
        ylabel="Ángulo (°)",
        
    )

    #adds major gridlines. whant that every grid appears for each 1 unit
    ax.grid(axis = 'y', color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

    aux_counter = 0
    counterwena = 0

    for pl,c in zip(wenas, wenascolor):

        sub_time = time[aux_counter:aux_counter+len(pl)]

        # if sub_time and pl has different length then the element with more lenght is
        # cutted to the length of the other element
        if len(sub_time) != len(pl):
            if len(sub_time) > len(pl):
                sub_time = sub_time[:len(pl)]
            else:
                pl = pl[:len(sub_time)]

        ax.plot(sub_time, pl, color = c)
        aux_counter += len(pl)
        counterwena += 1

    ax.scatter(time[-1], wenas[-1][-1], color = actual_color)
    ax.text(time[-1], wenas[-1][-1]+2, "{}°".format(wenas[-1][-1]), fontsize=12, color='#fff')
    ax.text(int(time[-1]*0.4), 90, "Repetición: {}".format(counter), fontsize=24, color='#fff')
    ax.set_ylim(-15,15)   

def plot_data():

    ani = animation.FuncAnimation(fig, my_function, interval=100)
    plt.show()



if __name__ == "__main__":

    print("Pasamos por acá")
    # Crear un socket de cliente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectar al servidor
        sock.connect((HOST, PORT))


        # Iniciar un hilo para recibir datos del servidor
        recv_thread = threading.Thread(target=receive_data, args=(sock,))
        recv_thread.start()
                    
        print("se activo el thread")
        threading.Thread(target=send_activate, args=(sock,)).start()

        while True:
            time.sleep(0.1)
            if plot:
                # create a figure
                global fig
                global ax
                fig = plt.figure(figsize = (14, 7), facecolor="#000000")
                ax = fig.add_subplot(1,1,1)
                ax.set_facecolor("#000000")
                ax.yaxis.label.set_color("#fff")
                ax.xaxis.label.set_color("#fff")
                ax.tick_params(axis='x', colors='#fff')
                ax.tick_params(axis='y', colors='#fff')
                ax.spines['bottom'].set_color('#fff')
                ax.spines['left'].set_color('#fff')
                ax.spines['top'].set_color('#fff')
                ax.spines['right'].set_color('#fff')
                ax.spines['top'].set_linewidth(2)
                ax.spines['right'].set_linewidth(2)
                ax.spines['bottom'].set_linewidth(2)
                ax.spines['left'].set_linewidth(2)
                # set fontsizes
                plt.rcParams['font.size'] = 14
                ax.xaxis.label.set_fontsize(16)
                ax.yaxis.label.set_fontsize(16)
                

                plot_data()
                plot = False
                break




                
        # Esperar a que ambos hilos terminen
        recv_thread.join()
        
        sys.exit(0)
        # send_thread.join()


