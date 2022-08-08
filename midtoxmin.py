import glob
import os


def re_txt(path,savepath):
    dataset_parameter = []
    with open(path, "r") as f:

        sourceInLine = f.readlines()

        for line in sourceInLine:
            temp1 = line.strip('\n')
            temp2 = temp1.strip(' ')
            temp3 = temp2.split(' ')

            dataset_parameter.append(temp3)
        for i in range(len(dataset_parameter)):
            a = float(dataset_parameter[i][1])
            b = float(dataset_parameter[i][2])
            c = float(dataset_parameter[i][3])
            d = float(dataset_parameter[i][4])

            dataset_parameter[i][1] = format(a - c / 2, '.5f')  # xmin
            dataset_parameter[i][2] = format(a + c / 2, '.5f')  # ymin
            dataset_parameter[i][3] = format(b - d / 2, '.5f')  # xmax
            dataset_parameter[i][4] = format(b - d / 2, '.5f')  # ymax


        with open(savepath, 'w') as f:
            for i in range(len(dataset_parameter)):
                f.write(dataset_parameter[i][0] + ' ' + dataset_parameter[i][1] + ' '
                        + dataset_parameter[i][2] + ' ' + dataset_parameter[i][3] + ' ' + dataset_parameter[i][4] + '\n'
                        )

        print(dataset_parameter)




file_dir = "D:/CT-7/yolov5-master/runs/detect/exp4/labels"

for root, dirs, files in os.walk(file_dir, topdown=False):
    print(root)
    print(root+'/'+files[0])
    print(len(files))

    for i in range(len(files)):
        path = root + '/' + files[i]
        savepath = file_dir + '/' + files[i]
        re_txt(path,savepath)