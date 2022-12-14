ТЕСТИРОВАНИЕ:
![image](https://user-images.githubusercontent.com/102906241/206798730-ddd93654-191b-43c6-9e25-c1cef207c105.png)
![image](https://user-images.githubusercontent.com/102906241/206798752-35b153fc-5e84-46f1-86b3-29f4a6e7797d.png)

ПРОФИЛИРОВАНИЕ:

Время выполнения прежнего метода обработки даты занимает 0.029 секунд

![image](https://user-images.githubusercontent.com/102906241/206798785-3d319fc3-a1cf-4019-b199-041ed2640328.png)

Теперь заменим прежний метод на метод, который использует библиотеку Arrow. Результат по времени выполнения получился еще больше - 0.096 секунд
![image](https://user-images.githubusercontent.com/102906241/206798814-9bacb564-8543-4d45-95ed-1895563a36cc.png)

Теперь снова заменим метод, но теперь на метод с использованием библиотеки Maya. Результат лучше, но все равно долго
![image](https://user-images.githubusercontent.com/102906241/206798856-1828aac1-6f89-46c4-8b7f-cb6436fb18ef.png)

В конце концов, попробуем применить метод, которой просто берёт срез из строки с датой. Время его выполнения существенно быстрее всех предыдущих - 0 секунд. Оставим его в программе, а остальные методы закомментируем

![image](https://user-images.githubusercontent.com/102906241/206798892-1170015e-6f2c-402d-a3c4-d94440bab5ad.png)

3.2.1

Скриншот разделенных csv-файлов

![image](https://user-images.githubusercontent.com/102906241/206799052-272bf4f1-e159-4f51-986d-2847e568602a.png)

3.2.2

Время выполнения программы без многопоточности: 
![image](https://user-images.githubusercontent.com/102906241/206871657-6c2872b1-5532-4cb9-acc4-fec69f11fb9b.png)

Время выполнения программы с многопоточностью:
![image](https://user-images.githubusercontent.com/102906241/206871537-73ee5cac-34e3-4056-8a6f-3f4751ced375.png)

3.3.1

Скриншот частотности, с которой встречаются различные валюты за 2003 – 2022 года:

![image](https://user-images.githubusercontent.com/102906241/208976782-e024ba2f-0a4e-41a1-8798-50ef5e529d69.png)
