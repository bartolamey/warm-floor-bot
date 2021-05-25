
from fpdf import FPDF
import os.path


def create_pdf():

    pdf = FPDF()

#-------------Данные для расчёта------------------------------------------------------------------------------
    name_file = open('name.txt', 'r')
    name = name_file.read()

    address_file = open('vendor/kermi/var/address.txt', 'r')
    address = address_file.read()

    area_file = open('vendor/kermi/var/area.txt', 'r')
    area = area_file.read()

    #Утеплен ли дом
    warm_house_file = open('vendor/kermi/var/warm_house.txt', 'r')
    warm_house = warm_house_file.read()

    #кол-во комнат
    number_of_rooms_file = open('vendor/kermi/var/number_of_rooms.txt', 'r')
    number_of_rooms = number_of_rooms_file.read()

#------------Прайс--------------------------------------------------------------------------------------------
    cena_truba = 0.75
    kermi_2    = 88.19
    kermi_3    = 112.21
    kermi_4    = 136.24
    kermi_5    = 160.27
    kermi_6    = 184.29
    kermi_7    = 208.35
    kermi_8    = 232.32
    kermi_9    = 256.34
    kermi_10   = 301.36
    kermi_11   = 328.75
    kermi_12   = 356.15

#------------------------Расчёт-------------------------------------------------------------------------------

    # 2 строка:  
    #Расчёт площади трубы в зависимости от утепления дома
    if int(warm_house) >= 1:    
        truba = float(area) / 0.15
    else:
        truba = float(area) / 0.10

    # 3 строка:
    #В распределителя
    if int(number_of_rooms) == 2:
        kermi = kermi_2
    elif int(number_of_rooms) == 3:
        kermi = kermi_3
    elif int(number_of_rooms) == 4:
        kermi = kermi_4
    elif int(number_of_rooms) == 5:
        kermi = kermi_5
    elif int(number_of_rooms) == 6:
        kermi = kermi_6
    elif int(number_of_rooms) == 7:
        kermi = kermi_7
    elif int(number_of_rooms) == 8:
        kermi = kermi_8
    elif int(number_of_rooms) == 9:
        kermi = kermi_9
    elif int(number_of_rooms) == 10:
        kermi = kermi_10
    elif int(number_of_rooms) == 11:
        kermi = kermi_11
    elif int(number_of_rooms) == 12:
       kermi = kermi_12

    # Итого:
    itogo = float(cena_truba * truba) + kermi


#----------PDF---------------------------------------------------------------------------------------------------

    pdf.add_page()
    pdf.add_font('GOST_A',   '', 'GOST_A_.ttf', uni=True)
    pdf.add_font('GOST_A_I', '', 'GOST_A_I.ttf', uni=True)
    pdf.add_font('GOST_A_B', '', 'GOST_A_B.ttf', uni=True)

    #Логотип
    pdf.image('img/logo.jpg', 180, 9, 20)

    # Спецификация отопления теплых полов
    pdf.set_font('GOST_A_B', size=18)
    pdf.cell(45)
    pdf.cell(0, 6, 'Спецификация отопления теплых полов', ln=1)

    #Заказчик
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(-1)
    pdf.cell(0, 10, 'Заказчик: ' + name, ln=1)                     #Добавить имя пользователя

    #Адрес
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(146)
    pdf.cell(0, -10, 'Адрес обьекта: ' + address, ln=1)         #Добавить адрес обьекта

    #Бот-конструктор
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(-1)
    pdf.cell(0, 20, 'Менеджер: Бот-конструктор', ln=1)                     #Добавить имя пользователя

    # Разрыв линии
    pdf.ln(1)

    #Первый абзац
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(65)
    pdf.cell(0, 5, txt='Тут должно что то быть', ln=1)
    pdf.set_font('GOST_A_I', size=11)
    pdf.cell(-1)
    pdf.cell(0, 5, txt='        Отопление теплым полом самое эффективное. Над черновым полом укладывается утеплитель, на котором крепится труба. После этого', ln=1)
    pdf.cell(0, 5, txt='«пирог пола» заливается чистовой стяжкой 6-8 см. В трубу идет вода низкой температуры (максимально до 55 градусов, фактически не выше 32 ', ln=1)
    pdf.cell(0, 5, txt='градусов). В результате на поверхности пола будут комфортные +23-26 градусов. При использовании обогрева полом, значительно уменьшается', ln=1)
    pdf.cell(0, 5, txt='кол-во пыли.', ln=1)
    pdf.ln(3)

    #Второй абзац
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(65)
    pdf.cell(0, 5, txt='Гарантия и качество', ln=1)

    pdf.set_font('GOST_A_I', size=11)
    pdf.cell(-1)
    pdf.cell(0, 5, txt='      Гарантия на трубопроводы 15 лет. Система теплого пола , благодаря совершенству конструкции составных элементов, а также их взаимному', ln=1)
    pdf.cell(0, 5, txt='соответствию, обеспечивает срок службы 50 лет. Это подтверждается испытаниями и исследованиями в современной лаборатории, и в ', ln=1)
    pdf.cell(0, 5, txt='крупнейших европейских сертификационных институтах.', ln=1)
    pdf.ln(3)

    #Третий абзац
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(65)
    pdf.cell(0, 5, txt='Технологические преимущества', ln=1)

    pdf.set_font('GOST_A_I', size=11)
    pdf.cell(-1)
    pdf.cell(0, 5, txt='- Трубы PE-RT производятся в соответствии с нормой PN-EN ISO 22391-2 из высококачественного полиэтилена соотвествующеготипа.', ln=1)
    pdf.cell(0, 5, txt='- Труба с антидиффузионной защитой , отвечающей требованиям нормы DIN 4726, защищающей от проникновения кислорода внутрь системы и', ln=1)
    pdf.cell(0, 5, txt='тем самым предохраняющей от возможного завоздушивания и коррозии арматуры.', ln=1)
    pdf.ln(3)

    #Фото
    pdf.image('img/1.png', 10, 110, 40)
    pdf.image('img/2.png', 48, 110, 100)
    pdf.image('img/3.png', 148, 110, 54)
    pdf.ln(50)

    #Таблица
    pdf.set_font("GOST_A_B", size=12)
    #1 строка
    pdf.cell(5, 5, txt='№', border=1, align='C')
    pdf.cell(115, 5, txt='Наименование', border=1, align='C')
    pdf.cell(12, 5, txt='ед.изм', border=1, align='C')
    pdf.cell(12, 5, txt='кол-во', border=1, align='C')
    pdf.cell(24, 5, txt='Цена, EUR', border=1, align='C')
    pdf.cell(24, 5, txt='Стоимость EUR', border=1, align='C')
    pdf.ln(5)

    #2 строка
    pdf.set_font("GOST_A_B", size=12)
    pdf.cell(5, 5, txt='1', border=1, align='C')
    pdf.cell(115, 5, txt='Труба полиэтилен PE-RT-5 Kermi x-net 16х2', border=1)
    pdf.cell(12, 5, txt='м', border=1, align='C')
    pdf.cell(12, 5, txt=str(round(truba, 2)), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(cena_truba, 2)), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(float(cena_truba * truba), 2)), border=1, align='C')
    pdf.ln(5)

    #3 строка
    pdf.cell(5, 5, txt='2', border=1, align='C')
    pdf.cell(115, 5, txt='Распределитель Kermi FT ' + str(number_of_rooms) + ' с расходомерами, на ' + str(number_of_rooms) + ' конт', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt='1', border=1, align='C')
    pdf.cell(24, 5, txt=str(kermi), border=1, align='C')
    pdf.cell(24, 5, txt=str(kermi), border=1, align='C')
    pdf.ln(5)

    #4 строка
    pdf.cell(5, 5, txt='3', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #5 строка
    pdf.cell(5, 5, txt='4', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #6 строка
    pdf.cell(5, 5, txt='5', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #7 строка
    pdf.cell(5, 5, txt='6', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #8 строка
    pdf.cell(5, 5, txt='7', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #9 строка
    pdf.cell(5, 5, txt='8', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #10 строка
    pdf.cell(5, 5, txt='9', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #11 строка
    pdf.cell(5, 5, txt='10', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #12 строка
    pdf.cell(5, 5, txt='11', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #13 строка
    pdf.cell(5, 5, txt='12', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #14 строка
    pdf.cell(5, 5, txt='13', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #15 строка
    pdf.cell(5, 5, txt='14', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #16 строка
    pdf.cell(5, 5, txt='15', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #17 строка
    pdf.cell(5, 5, txt='16', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #18 строка
    pdf.cell(5, 5, txt='17', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #19 строка
    pdf.cell(5, 5, txt='18', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #20 строка
    pdf.cell(5, 5, txt='19', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #21 строка
    pdf.cell(5, 5, txt='20', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #22 строка
    pdf.cell(5, 5, txt='21', border=1, align='C')
    pdf.cell(115, 5, txt='', border=1)
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.ln(5)

    #Итого
    pdf.cell(5, 5, txt='22', border=1, align='C')
    pdf.set_font('GOST_A_B', size=12)
    pdf.cell(115, 5, txt='Итого Евро:', border=1, align='R')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(12, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt='', border=1, align='C')
    pdf.cell(24, 5, txt=str(round(itogo, 2)), border=1, align='C')

    pdf.ln(5)

    #PDF-ка
    pdf.output('vendor/kermi/your_calculation.pdf')


