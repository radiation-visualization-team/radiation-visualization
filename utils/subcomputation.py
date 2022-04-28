# import numpy as np
# antennas和sub_antenna都是列表
# antennas: 大小为mxn, 内部存放的是图的实例化对象
# sub_antenna: 元素与subArray中的文本框有位置映射关系，映射关系在img中
# [('8', '8'), ('8', '16'), ('8', '32'), ('16', '16'), ('16', '32'), ('16', '64'), ('32', '32'), ('32', '64'),('64', '64')]
import numpy as np


class MatrixPlus:
    def __init__(self, antennas, sub_antenna, size):
        self.antennas = antennas
        self.sub_antenna = sub_antenna
        self.size = size
        self.matrixplus = self.create_matrixplus()  # 加上外权重的实例图列表，大小同antennas一致

    def pic_8_8(self):  # √
        return self.antennas  # 当你为8*8大小的时候无外权重

    def pic_8_16(self):  # √
        self.addweight_matrix(0, 1, self.sub_antenna[0])  # 外权重添加至0,1
        return self.antennas

    def pic_8_32(self):  # √
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1]  # 外权重0,1添加至0,1
        weight_2 = self.sub_antenna[0] + self.sub_antenna[2]
        self.addweight_matrix(0, 1, weight_1)
        self.addweight_matrix(2, 3, weight_2)
        return self.antennas

    def pic_16_16(self):  # √
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1]
        weight_2 = self.sub_antenna[0] + self.sub_antenna[2]
        self.addweight_matrix(0, 2, weight_1)
        self.addweight_matrix(1, 3, weight_2)
        return self.antennas

    def pic_16_32(self):  # √
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3]
        weight_2 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4]
        weight_3 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5]
        weight_4 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6]
        self.addweight_matrix(0, 4, weight_1)
        self.addweight_matrix(1, 5, weight_2)
        self.addweight_matrix(2, 6, weight_3)
        self.addweight_matrix(3, 7, weight_4)
        return self.antennas

    def pic_16_64(self):  # √
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7]
        weight_2 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[8]
        weight_3 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4] + self.sub_antenna[9]
        weight_4 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4] + self.sub_antenna[10]
        weight_5 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5] + self.sub_antenna[11]
        weight_6 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5] + self.sub_antenna[12]
        weight_7 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[13]
        weight_8 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14]
        self.addweight_matrix(0, 8, weight_1)
        self.addweight_matrix(1, 9, weight_2)
        self.addweight_matrix(2, 10, weight_3)
        self.addweight_matrix(3, 11, weight_4)
        self.addweight_matrix(4, 12, weight_5)
        self.addweight_matrix(5, 13, weight_6)
        self.addweight_matrix(6, 14, weight_7)
        self.addweight_matrix(7, 15, weight_8)
        return self.antennas

    def pic_32_32(self):  # √
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7]
        weight_2 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[8]
        weight_3 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[9]
        weight_4 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[10]
        weight_5 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[11]
        weight_6 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[12]
        weight_7 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[13]
        weight_8 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14]
        self.addweight_matrix(0, 4, weight_1)
        self.addweight_matrix(1, 5, weight_2)
        self.addweight_matrix(2, 6, weight_3)
        self.addweight_matrix(3, 7, weight_4)
        self.addweight_matrix(8, 12, weight_5)
        self.addweight_matrix(9, 13, weight_6)
        self.addweight_matrix(10, 14, weight_7)
        self.addweight_matrix(11, 15, weight_8)
        return self.antennas

    def pic_32_64(self):  # √
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7] + \
                   self.sub_antenna[15]
        weight_2 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7] + \
                   self.sub_antenna[16]
        weight_3 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[11] + \
                   self.sub_antenna[23]
        weight_4 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[11] + \
                   self.sub_antenna[24]
        weight_5 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4] + self.sub_antenna[8] + \
                   self.sub_antenna[17]
        weight_6 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4] + self.sub_antenna[8] + \
                   self.sub_antenna[18]
        weight_7 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4] + self.sub_antenna[12] + \
                   self.sub_antenna[25]
        weight_8 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[4] + self.sub_antenna[12] + \
                   self.sub_antenna[26]
        weight_9 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5] + self.sub_antenna[9] + \
                   self.sub_antenna[19]
        weight_10 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5] + self.sub_antenna[9] + \
                    self.sub_antenna[20]
        weight_11 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5] + self.sub_antenna[13] + \
                    self.sub_antenna[27]
        weight_12 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[5] + self.sub_antenna[13] + \
                    self.sub_antenna[28]
        weight_13 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[10] + \
                    self.sub_antenna[21]
        weight_14 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[10] + \
                    self.sub_antenna[22]
        weight_15 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14] + \
                    self.sub_antenna[29]
        weight_16 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14] + \
                    self.sub_antenna[30]
        self.addweight_matrix(0, 8, weight_1)
        self.addweight_matrix(1, 9, weight_2)
        self.addweight_matrix(16, 24, weight_3)
        self.addweight_matrix(17, 25, weight_4)
        self.addweight_matrix(2, 10, weight_5)
        self.addweight_matrix(3, 11, weight_6)
        self.addweight_matrix(18, 26, weight_7)
        self.addweight_matrix(19, 27, weight_8)
        self.addweight_matrix(4, 12, weight_9)
        self.addweight_matrix(5, 13, weight_10)
        self.addweight_matrix(20, 28, weight_11)
        self.addweight_matrix(21, 29, weight_12)
        self.addweight_matrix(6, 14, weight_13)
        self.addweight_matrix(7, 15, weight_14)
        self.addweight_matrix(22, 30, weight_15)
        self.addweight_matrix(23, 31, weight_16)
        return self.antennas

    def pic_64_64(self):
        weight_1 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7] + \
                   self.sub_antenna[15] + self.sub_antenna[31]
        weight_2 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7] + \
                   self.sub_antenna[15] + self.sub_antenna[32]
        weight_3 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7] + \
                   self.sub_antenna[19] + self.sub_antenna[39]
        weight_4 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[7] + \
                   self.sub_antenna[19] + self.sub_antenna[40]
        weight_5 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[8] + \
                   self.sub_antenna[16] + self.sub_antenna[33]
        weight_6 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[8] + \
                   self.sub_antenna[16] + self.sub_antenna[34]
        weight_7 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[8] + \
                   self.sub_antenna[20] + self.sub_antenna[41]
        weight_8 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[3] + self.sub_antenna[8] + \
                   self.sub_antenna[20] + self.sub_antenna[42]
        weight_9 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[11] + \
                   self.sub_antenna[23] + self.sub_antenna[47]
        weight_10 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[11] + \
                    self.sub_antenna[23] + self.sub_antenna[48]
        weight_11 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[11] + \
                    self.sub_antenna[27] + self.sub_antenna[55]
        weight_12 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[11] + \
                    self.sub_antenna[27] + self.sub_antenna[56]
        weight_13 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[12] + \
                    self.sub_antenna[24] + self.sub_antenna[49]
        weight_14 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[12] + \
                    self.sub_antenna[24] + self.sub_antenna[50]
        weight_15 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[12] + \
                    self.sub_antenna[28] + self.sub_antenna[57]
        weight_16 = self.sub_antenna[0] + self.sub_antenna[1] + self.sub_antenna[5] + self.sub_antenna[12] + \
                    self.sub_antenna[28] + self.sub_antenna[58]
        weight_17 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[9] + \
                    self.sub_antenna[17] + self.sub_antenna[35]
        weight_18 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[9] + \
                    self.sub_antenna[17] + self.sub_antenna[36]
        weight_19 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[9] + \
                    self.sub_antenna[21] + self.sub_antenna[43]
        weight_20 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[9] + \
                    self.sub_antenna[21] + self.sub_antenna[44]
        weight_21 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[10] + \
                    self.sub_antenna[18] + self.sub_antenna[37]
        weight_22 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[10] + \
                    self.sub_antenna[18] + self.sub_antenna[38]
        weight_23 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[10] + \
                    self.sub_antenna[22] + self.sub_antenna[45]
        weight_24 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[4] + self.sub_antenna[10] + \
                    self.sub_antenna[22] + self.sub_antenna[46]
        weight_25 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[13] + \
                    self.sub_antenna[25] + self.sub_antenna[51]
        weight_26 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[13] + \
                    self.sub_antenna[25] + self.sub_antenna[52]
        weight_27 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[13] + \
                    self.sub_antenna[29] + self.sub_antenna[59]
        weight_28 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[13] + \
                    self.sub_antenna[29] + self.sub_antenna[60]
        weight_29 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14] + \
                    self.sub_antenna[26] + self.sub_antenna[53]
        weight_30 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14] + \
                    self.sub_antenna[26] + self.sub_antenna[54]
        weight_31 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14] + \
                    self.sub_antenna[30] + self.sub_antenna[61]
        weight_32 = self.sub_antenna[0] + self.sub_antenna[2] + self.sub_antenna[6] + self.sub_antenna[14] + \
                    self.sub_antenna[30] + self.sub_antenna[62]
        self.addweight_matrix(0, 8, weight_1)
        self.addweight_matrix(1, 9, weight_2)
        self.addweight_matrix(16, 24, weight_3)
        self.addweight_matrix(17, 25, weight_4)
        self.addweight_matrix(2, 10, weight_5)
        self.addweight_matrix(3, 11, weight_6)
        self.addweight_matrix(18, 26, weight_7)
        self.addweight_matrix(19, 27, weight_8)
        self.addweight_matrix(32, 40, weight_9)
        self.addweight_matrix(33, 41, weight_10)
        self.addweight_matrix(48, 56, weight_11)
        self.addweight_matrix(49, 57, weight_12)
        self.addweight_matrix(34, 42, weight_13)
        self.addweight_matrix(35, 43, weight_14)
        self.addweight_matrix(50, 58, weight_15)
        self.addweight_matrix(51, 59, weight_16)
        self.addweight_matrix(4, 12, weight_17)
        self.addweight_matrix(5, 13, weight_18)
        self.addweight_matrix(20, 28, weight_19)
        self.addweight_matrix(21, 29, weight_20)
        self.addweight_matrix(6, 14, weight_21)
        self.addweight_matrix(7, 15, weight_22)
        self.addweight_matrix(22, 30, weight_23)
        self.addweight_matrix(23, 31, weight_24)
        self.addweight_matrix(36, 44, weight_25)
        self.addweight_matrix(37, 45, weight_26)
        self.addweight_matrix(52, 60, weight_27)
        self.addweight_matrix(53, 61, weight_28)
        self.addweight_matrix(38, 46, weight_29)
        self.addweight_matrix(39, 47, weight_30)
        self.addweight_matrix(54, 62, weight_31)
        self.addweight_matrix(55, 63, weight_32)
        return self.antennas

    # 将权重赋给对应图的矩阵(并转为array类型)
    def addweight_matrix(self, index_1, index_2, weight):  # index对应了实例化图列表中需要加权重的实例图索引
        self.antennas[index_1].matrix = np.array(self.antennas[index_1].matrix)
        self.antennas[index_2].matrix = np.array(self.antennas[index_2].matrix)
        self.antennas[index_1].matrix += weight
        self.antennas[index_2].matrix += weight

    def create_matrixplus(self):  # 识别不同大小的图，逐个添加对应外权重最后返回
        if self.size == ('8', '8'):
            return self.pic_8_8()
        elif self.size == ('8', '16'):
            return self.pic_8_16()
        elif self.size == ('8', '32'):
            return self.pic_8_32()
        elif self.size == ('16', '16'):
            return self.pic_16_16()
        elif self.size == ('16', '32'):
            return self.pic_16_32()
        elif self.size == ('16', '64'):
            return self.pic_16_64()
        elif self.size == ('32', '32'):
            return self.pic_32_32()
        elif self.size == ('32', '64'):
            return self.pic_32_64()
        elif self.size == ('64', '64'):
            return self.pic_64_64()
        else:
            print("input_size error")


if __name__ == "__main__":
    antennas = []
    sub_antenna = []
    # 这两个列表一定要直接用实例化的对象来进行matrixPlus的实例化，而不是传两个被赋值的列表，我这里的例程只是告诉你要传什么东西
    size = ('8', '8')
    matrixPlus = MatrixPlus(antennas, sub_antenna, size)  # 输入格式已写于最顶部注释
    # 实例化之后即完成权重加入，各部分已完成路径检查，若出现错误应当为逻辑错误，请直接联系小麦修改
