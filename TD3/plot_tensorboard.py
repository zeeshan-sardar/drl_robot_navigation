from matplotlib import pyplot as plt
from tensorflow.python.summary.summary_iterator import summary_iterator
loss = []
avgQ = []
maxQ = []

for summary in summary_iterator("./runs/Mar25_17-24-33_DESKTOP-FILNP1U/events.out.tfevents.1679754273.DESKTOP-FILNP1U.5826.0"):
    for value in summary.summary.value:
        if value.tag == "loss":
            # plt.plot(value.simple_value)
            # print("value",value.simple_value)
            loss.append(value.simple_value)
        if value.tag == "Av. Q":
            # plt.plot(value.simple_value)
            # print("value",value.simple_value)
            avgQ.append(value.simple_value)
        if value.tag == "Max. Q":
            # plt.plot(value.simple_value)
            # print("value",value.simple_value)
            maxQ.append(value.simple_value)
plt.figure(figsize=(10,6))
plt.plot(loss)
plt.xlabel("Steps", fontsize=16)
plt.ylabel("Loss", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("DDPG Loss", fontsize = 18)
plt.grid()

plt.figure(figsize=(10,6))
plt.plot(avgQ)
plt.xlabel("Steps", fontsize=16)
plt.ylabel("Avg Q", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("DDPG Average Q", fontsize = 20)
plt.grid()

plt.figure(figsize=(10,6))
plt.plot(maxQ)
plt.xlabel("Steps", fontsize=16)
plt.ylabel("Max Q", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("DDPG Max Q",fontsize = 18)
plt.grid()
plt.show()
