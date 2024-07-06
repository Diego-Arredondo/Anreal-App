import matplotlib.pyplot as plt 
import matplotlib.animation as animation


# create a figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []

# create animation

def animate(i, xs, ys):
    # read data from file
    data = open('data.txt', 'r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    # clear the axes
    ax.clear()
    # plot
    ax.plot(xs, ys)
    # format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (C)')
    plt.xlabel('Time')


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
