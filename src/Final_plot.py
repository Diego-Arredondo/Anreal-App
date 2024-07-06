from User import User
import matplotlib.pyplot as plt 

import numpy as np
from scipy.signal import savgol_filter

users = None

def plot_histogram(user_number = -1):

    global users

    if users is None:

        try:
            users = User.load_all()
        except:
            print("No users found")

    
    name = users[user_number].name
    maximos = users[user_number].maxs
    

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
    ax.set_ylim(-10,100)


    # set fontsizes
    plt.rcParams['font.size'] = 10
    ax.xaxis.label.set_fontsize(16)
    ax.yaxis.label.set_fontsize(16)

    #adds major gridlines
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    #set title white
    ax.title.set_color("#fff")



    # histograma de los valores de la variable maximos
    reps = np.arange(1, len(maximos)+1, 1)
    ax.bar(reps, maximos, width = 0.2)
    ax.scatter(reps, maximos, color='#fff', s=50)

    ax.plot(reps, maximos, color='#fff', linewidth=2, linestyle='dashed', marker='o', markerfacecolor='#fff', markersize=5)

    for ind, i in enumerate(maximos):
        ax.text(ind + 0.9, i + 3,"{}°".format(round(i,2)), fontsize=15, color='#fff')
        

    ax.set_xlim(0, len(maximos)+1)

    ax.set(
        title=f"Resumen sesión: {name}",
        xlabel="Repetición",
        ylabel="Ángulo (°)",
    )


    plt.show()


def plot_data(user_number = -1):
    global users

    if users is None:

        try:
            users = User.load_all()
        except:
            print("No users found")


    name = users[user_number].name
    ys = users[user_number].values
    ys = savgol_filter(ys, 100, 3)
    flags = users[user_number].flags


    # general plot configs
    fig = plt.figure(figsize = (16, 8), facecolor="#000000")
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
    
    ax.set(
        title=f"Resumen sesión: {name}",
        xlabel="Tiempo (s)",
        ylabel="Ángulo (°)",
        
    )

    #adds major gridlines
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    ax.set_ylim(-15,100)

    datos = []
    sublista_actual = []
    flag_anterior = None
    colors = []



    for flag, dato in zip(flags, ys):
        if flag != flag_anterior:
            colors.append('#1AB804' if flag==1 else '#FF0D8A') 
            if sublista_actual:
                datos.append(sublista_actual)
            sublista_actual = [dato]
        else:
            sublista_actual.append(dato)
        flag_anterior = flag
    if sublista_actual:
        datos.append(sublista_actual)


    counter = 0
    for dato, color in zip(datos, colors):

        sub_time = [x + counter for x in [i*0.02 for i in range(len(dato))]]

        ax.plot(sub_time, dato, color = color)
        counter += len(dato)*0.02
  

    plt.show()


if __name__ == "__main__":
    
    try:
        users = User.load_all()
    except:
        print("No users found")
    
    #print all users numbered by name, so the user can select one
    for i, user in enumerate(users):
        print(f"{i}: {user.name} : {user.description}")
    
    #ask user to select one
    user_number = int(input("Select user: "))

    plot_histogram(user_number)
    plot_data(user_number)