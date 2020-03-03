import pandas as pd
import matplotlib.pyplot as plt
#
# plt.style.use('ggplot')
# res = pd.read_csv("resnet44_benchmark_a0d5e4lr01_11111_0.0.csv")
# fixup = pd.read_csv("fixup_resnet44_benchmark_a0d5e4lr01_11111_0.0Meng_complete.csv")
# fig_1 = plt.figure(figsize=(8,4))
# ax_1 = fig_1.add_subplot(111)
#
#
# ax_1.set_ylabel("Loss")
# ax_1.set_xlabel("Epoch number")
# ax_1.plot(res["epoch"],res['train loss'])
# ax_1.plot(res["epoch"],res['test loss'])
#
# ax_1.plot(fixup["epoch"],fixup['train loss'])
# ax_1.plot(fixup["epoch"],fixup['test loss'])
#
# ax_1.legend(("resnet_44_train_loss","resnet_44_test_loss","fixup_44_train_loss","fixup_44_test_loss"))
# fig_2 = plt.figure(figsize=(8,4))
# ax_2 = fig_2.add_subplot(111)
#
#
# ax_2.set_ylabel("Acc")
# ax_2.set_xlabel("Epoch number")
#
# ax_2.plot(res["epoch"],res['train acc'])
# ax_2.plot(res["epoch"],res['test acc'])
#
# ax_2.plot(fixup["epoch"],fixup['train acc'])
# ax_2.plot(fixup["epoch"],fixup['test acc'])
#
# ax_2.legend(("resnet_44_train_acc","resnet_44_test_acc","fixup_44_train_acc","fixup_44_test_acc"))
#
# fig_1.savefig('44_loss.pdf',dpi = None,facecolor = 'w',edgecolor = 'w',orientation = 'portrait',papertype = None, format = 'pdf',transparent=False,bbox_inches=None,pad_inches=0.1,frameon = None, metadata = None)
# fig_2.savefig('44_acc.pdf',dpi = None,facecolor = 'w',edgecolor = 'w',orientation = 'portrait',papertype = None, format = 'pdf',transparent=False,bbox_inches=None,pad_inches=0.1,frameon = None, metadata = None)
# plt.show()



plt.style.use('ggplot')
tt1 = pd.read_csv("0.0SGDR_1T.csv")
tt10 = pd.read_csv("0.0SGDR_10T.csv")
tt50 = pd.read_csv("0.0SGDR_50T.csv")
tt100 = pd.read_csv("0.0SGDR_100T.csv")
tt200 = pd.read_csv("0.0SGDR_200T.csv")

fig_1 = plt.figure(figsize=(8,4))
ax_1 = fig_1.add_subplot(111)


ax_1.set_ylabel("Test Acc")
ax_1.set_xlabel("Epoch number")


ax_1.plot(tt1["epoch"],tt1['test acc'])
ax_1.plot(tt10["epoch"],tt10['test acc'])
ax_1.plot(tt50["epoch"],tt50['test acc'])
ax_1.plot(tt100["epoch"],tt100['test acc'])
ax_1.plot(tt200["epoch"],tt200['test acc'])
ax_1.legend(('1','10','50','100','200'))
plt.show()
