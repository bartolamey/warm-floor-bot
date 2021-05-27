
from fpdf import FPDF
import os.path
import math
import time



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

#------------Прайс в евро--------------------------------------------------------------------------------------------

    kermi_2           = 88.19
    kermi_3           = 112.21
    kermi_4           = 136.24
    kermi_5           = 160.27
    kermi_6           = 184.29
    kermi_7           = 208.35
    kermi_8           = 232.32
    kermi_9           = 256.34
    kermi_10          = 301.36
    kermi_11          = 328.75
    kermi_12          = 356.15
    cena_truba        = 0.75     #Труба полиэтилен PE-RT-5 Kermi x-net 16х2
    cena_tape         = 14.25    #Лента боковая Kermi x-net H 160 мм (бухта 25 м)
    cena_foil         = 0.93     #Пленка фольгированная 1мм с разметкой
    cena_hairpin      = 12.0     #Шпильки для теплого пола упак для такера, 250шт
    cena_thr_connect  = 2.48     #Резьбовое соединение Kermi x-net 16x2
    cena_metal_plast  = 1.71     #Труба металлопластиковая Kermi x-net MKV 20 x 2,0 
    cena_kran_pr      = 23.40    #Комплект кранов прямой 1"х3/4"
    cena_thread_adapt = 7.12     #Резьбой переходник Kermi x-net "1х25
    cena_kran_maevsk  = 1.10     #Кран маевского G1/2"
    cena_provodnik_tr = 1.14     #Проводник трубы Ø14-18
    cena_homut_tr_25  = 0.79     #Хомут одинарный с резиновым вкладышем для трубы 25
    cena_izol_tr_25   = 0.58     #Изоляция для труб Ø25 -28х9
    cena_skotch_50    = 3.15     #скотч для пленки (50 м)
    cena_enrgo_blue   = 0.42     #Энергофлекс Ø18*9, синяя
    cena_enrgo_red    = 0.42     #Энергофлекс Ø18*9, красная


#------------------------Расчёт-------------------------------------------------------------------------------

    # 2 строка:  
    #Расчёт площади трубы в зависимости от утепления дома
    if int(warm_house) >= 1:    
        truba = float(area) / 0.15
    else:
        truba = float(area) / 0.10

    summ_truba = float(cena_truba * truba)

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

    # 4 строка:
    tape      = math.ceil((float(area) * 2) / 25)
    summ_tape = float(tape * cena_tape)

    # 5 строка
    foil      = math.ceil(float(area) / 0.9)
    summ_foil = float(foil * cena_foil)

    # 6 строка
    hairpin      = math.ceil(float((truba * 3) / 250))
    summ_hairpin = float(hairpin * cena_hairpin)

     # 7 строка
    thr_connect      = int(number_of_rooms) * 2
    summ_thr_connect = float(thr_connect) * cena_thr_connect

    # 8 Строка
    metal_plast      = math.ceil(float(area) / 5.7)
    summ_metal_plast = float(metal_plast * cena_metal_plast)

    # 9 Строка
    kran_pr = 1 #Возможно потребуется добавить логику при увеличении кол-во распределителей
    summ_kran_pr = kran_pr * cena_kran_pr

    # 10 Строка
    thread_adapter    = kran_pr * 2
    summ_thread_adapt = float(thread_adapter * cena_thread_adapt)

    # 11 Строка
    kran_maevsk      = thr_connect + 1 #Возможно потребуется добавить логику при увеличении кол-во распределителей
    summ_kran_maevsk = cena_kran_maevsk * kran_maevsk

    # 12 Строка
    provodnik_tr      = int(number_of_rooms) * 2
    summ_provodnik_tr = cena_provodnik_tr * provodnik_tr

    # 13 Строка
    homut_tr_25      = 21
    summ_homut_tr_25 = cena_homut_tr_25 * float(homut_tr_25)

    # 14 Строка
    izol_tr_25      = 21
    summ_izol_tr_25 = cena_izol_tr_25 * float(izol_tr_25)

    # 15 Строка
    skotch_50       = round(int(area) / 0.9 / 50)
    summ_skotch_50  = float(skotch_50) * cena_skotch_50

    # 16 Строка
    enrgo_blue      = number_of_rooms
    summ_enrgo_blue = float(enrgo_blue) * cena_enrgo_blue

    # 17 Строка
    enrgo_red      = number_of_rooms
    summ_enrgo_red = float(enrgo_red) * cena_enrgo_red

    # Итого:
    itogo = summ_truba + kermi + summ_tape + summ_foil + summ_hairpin + summ_thr_connect + summ_metal_plast + summ_kran_pr + summ_thread_adapt + summ_kran_maevsk + summ_provodnik_tr + summ_homut_tr_25 + summ_izol_tr_25 + summ_skotch_50 + summ_enrgo_blue + summ_enrgo_red


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
    pdf.cell(12, 5, txt=str(math.ceil(truba)), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(cena_truba, 2)), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(float(summ_truba), 2)), border=1, align='C')
    pdf.ln(5)

    #3 строка
    pdf.cell(5, 5, txt='2', border=1, align='C')
    pdf.cell(115, 5, txt='Распределитель Kermi FT ' + str(number_of_rooms) + ' с расходомерами, на ' + str(number_of_rooms) + ' конт', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt='1', border=1, align='C')
    pdf.cell(24, 5, txt=str(kermi), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(kermi, 2)), border=1, align='C')
    pdf.ln(5)

    #4 строка
    pdf.cell(5, 5, txt='3', border=1, align='C')
    pdf.cell(115, 5, txt='Лента боковая Kermi x-net H 160 мм (бухта 25 м)', border=1)
    pdf.cell(12, 5, txt='бух', border=1, align='C')
    pdf.cell(12, 5, txt=str(round(tape, 0)), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_tape), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_tape, 2)), border=1, align='C')
    pdf.ln(5)

    #5 строка
    pdf.cell(5, 5, txt='4', border=1, align='C')
    pdf.cell(115, 5, txt='Пленка фольгированная 1мм с разметкой', border=1)
    pdf.cell(12, 5, txt='m2', border=1, align='C')
    pdf.cell(12, 5, txt=str(round(foil, 0)), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_foil), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_foil, 2)), border=1, align='C')
    pdf.ln(5)

    #6 строка
    pdf.cell(5, 5, txt='5', border=1, align='C')
    pdf.cell(115, 5, txt='Шпильки для теплого пола упак для такера, 250шт', border=1)
    pdf.cell(12, 5, txt='упк', border=1, align='C')
    pdf.cell(12, 5, txt=str(hairpin), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_hairpin), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_hairpin, 2)), border=1, align='C')
    pdf.ln(5)

    #7 строка
    pdf.cell(5, 5, txt='6', border=1, align='C')
    pdf.cell(115, 5, txt='Резьбовое соединение Kermi x-net 16x2', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(thr_connect), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_thr_connect), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_thr_connect, 2)), border=1, align='C')
    pdf.ln(5)

    #8 строка
    pdf.cell(5, 5, txt='7', border=1, align='C')
    pdf.cell(115, 5, txt='Труба металлопластиковая Kermi x-net MKV 20 x 2,0', border=1)
    pdf.cell(12, 5, txt='м', border=1, align='C')
    pdf.cell(12, 5, txt=str(metal_plast), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_metal_plast), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_metal_plast, 2)), border=1, align='C')
    pdf.ln(5)

    #9 строка
    pdf.cell(5, 5, txt='8', border=1, align='C')
    pdf.cell(115, 5, txt='Комплект кранов прямой 1"х3/4"', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(kran_pr), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_kran_pr), border=1, align='C')
    pdf.cell(24, 5, txt=str(round((summ_kran_pr), 2)), border=1, align='C')
    pdf.ln(5)

    #10 строка
    pdf.cell(5, 5, txt='9', border=1, align='C')
    pdf.cell(115, 5, txt='Резьбой переходник Kermi x-net "1х25', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(thread_adapter), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_thread_adapt), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_thread_adapt, 2)), border=1, align='C')
    pdf.ln(5)

    #11 строка
    pdf.cell(5, 5, txt='10', border=1, align='C')
    pdf.cell(115, 5, txt='Кран маевского G1/2"', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(kran_maevsk), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_kran_maevsk), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_kran_maevsk, 2)), border=1, align='C')
    pdf.ln(5)

    #12 строка
    pdf.cell(5, 5, txt='11', border=1, align='C')
    pdf.cell(115, 5, txt='Проводник трубы Ø14-18', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(provodnik_tr), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_provodnik_tr), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_provodnik_tr, 2)), border=1, align='C')
    pdf.ln(5)

    #13 строка
    pdf.cell(5, 5, txt='12', border=1, align='C')
    pdf.cell(115, 5, txt='Хомут одинарный с резиновым вкладышем для трубы 25', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(homut_tr_25), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_homut_tr_25), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_homut_tr_25, 2)), border=1, align='C')
    pdf.ln(5)

    #14 строка
    pdf.cell(5, 5, txt='13', border=1, align='C')
    pdf.cell(115, 5, txt='Изоляция для труб Ø25 -28х9', border=1)
    pdf.cell(12, 5, txt='м', border=1, align='C')
    pdf.cell(12, 5, txt=str(izol_tr_25), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_izol_tr_25), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_izol_tr_25, 2)), border=1, align='C')
    pdf.ln(5)

    #15 строка
    pdf.cell(5, 5, txt='14', border=1, align='C')
    pdf.cell(115, 5, txt='Скотч для пленки (50 м)', border=1)
    pdf.cell(12, 5, txt='шт', border=1, align='C')
    pdf.cell(12, 5, txt=str(skotch_50), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_skotch_50), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_skotch_50, 2)), border=1, align='C')
    pdf.ln(5)

    #16 строка
    pdf.cell(5, 5, txt='15', border=1, align='C')
    pdf.cell(115, 5, txt='Энергофлекс Ø18*9, синяя', border=1)
    pdf.cell(12, 5, txt='м', border=1, align='C')
    pdf.cell(12, 5, txt=str(enrgo_blue), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_enrgo_blue), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_enrgo_blue, 2)), border=1, align='C')
    pdf.ln(5)

    #17 строка
    pdf.cell(5, 5, txt='15', border=1, align='C')
    pdf.cell(115, 5, txt='Энергофлекс Ø18*9, красная', border=1)
    pdf.cell(12, 5, txt='м', border=1, align='C')
    pdf.cell(12, 5, txt=str(enrgo_red), border=1, align='C')
    pdf.cell(24, 5, txt=str(cena_enrgo_red), border=1, align='C')
    pdf.cell(24, 5, txt=str(round(summ_enrgo_red, 2)), border=1, align='C')
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
    time.sleep(1)
    pdf.output('vendor/kermi/your_calculation.pdf')


