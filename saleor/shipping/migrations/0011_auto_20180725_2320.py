# Generated by Django 2.0.3 on 2018-07-25 20:20

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0010_auto_20180719_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Rest of World'), ('AF', 'Афганистан'), ('AL', 'Албания'), ('DZ', 'Алжир'), ('AD', 'Андорра'), ('AO', 'Ангола'), ('AI', 'Ангилья'), ('AQ', 'Антарктида'), ('AR', 'Аргентина'), ('AM', 'Армения'), ('AW', 'Аруба'), ('AU', 'Австралия'), ('AT', 'Австрия'), ('AZ', 'Азербайджан'), ('BH', 'Бахрейн'), ('BD', 'Бангладеш'), ('BB', 'Барбадос'), ('BY', 'Беларусь'), ('BE', 'Бельгия'), ('BZ', 'Белиз'), ('BJ', 'Бенин'), ('BT', 'Бутан'), ('BO', 'Боливия'), ('BW', 'Ботсвана'), ('BR', 'Бразилия'), ('BN', 'Бруней'), ('BG', 'Болгария'), ('BI', 'Бурунди'), ('KH', 'Камбоджа'), ('CM', 'Камерун'), ('CA', 'Канада'), ('TD', 'Чад'), ('CL', 'Чили'), ('CN', 'Китай'), ('CO', 'Колумбия'), ('CG', 'Конго'), ('HR', 'Хорватия'), ('CU', 'Куба'), ('CW', 'Кюрасао'), ('CY', 'Кипр'), ('CZ', 'Чехия'), ('DK', 'Дания'), ('DJ', 'Джибути'), ('DM', 'Доминика'), ('EC', 'Эквадор'), ('EG', 'Египет'), ('SV', 'Сальвадор'), ('ER', 'Эритрея'), ('EE', 'Эстония'), ('ET', 'Эфиопия'), ('FJ', 'Фиджи'), ('FI', 'Финляндия'), ('FR', 'Франция'), ('GA', 'Габон'), ('GM', 'Гамбия'), ('GE', 'Грузия'), ('DE', 'Германия'), ('GH', 'Гана'), ('GI', 'Гибралтар'), ('GR', 'Греция'), ('GL', 'Гренландия'), ('GD', 'Гренада'), ('GP', 'Гваделупа'), ('GU', 'Гуам'), ('GT', 'Гватемала'), ('GG', 'Гернси'), ('GN', 'Гвинея'), ('GY', 'Гайана'), ('HT', 'Гаити'), ('HN', 'Гондурас'), ('HK', 'Гонконг'), ('HU', 'Венгрия'), ('IS', 'Исландия'), ('IN', 'Индия'), ('ID', 'Индонезия'), ('IR', 'Иран'), ('IQ', 'Ирак'), ('IE', 'Ирландия'), ('IL', 'Израиль'), ('IT', 'Италия'), ('JM', 'Ямайка'), ('JP', 'Япония'), ('JE', 'Джерси'), ('JO', 'Иордания'), ('KZ', 'Казахстан'), ('KE', 'Кения'), ('KI', 'Кирибати'), ('KW', 'Кувейт'), ('KG', 'Киргизия'), ('LA', 'Лаос'), ('LV', 'Латвия'), ('LB', 'Ливан'), ('LS', 'Лесото'), ('LR', 'Либерии'), ('LY', 'Ливия'), ('LI', 'Лихтенштейн'), ('LT', 'Литва'), ('LU', 'Люксембург'), ('MO', 'Макао'), ('MK', 'Македония'), ('MG', 'Мадагаскар'), ('MW', 'Малави'), ('MY', 'Малайзия'), ('MV', 'Мальдивы'), ('ML', 'Мали'), ('MT', 'Мальта'), ('MQ', 'Мартиника'), ('MR', 'Мавритания'), ('MU', 'Маврикий'), ('YT', 'Майотта'), ('MX', 'Мексика'), ('MD', 'Молдавия'), ('MC', 'Монако'), ('MN', 'Монголия'), ('ME', 'Черногория'), ('MS', 'Монтсеррат'), ('MA', 'Марокко'), ('MZ', 'Мозамбик'), ('MM', 'Мьянмы'), ('NA', 'Намибия'), ('NR', 'Науру'), ('NP', 'Непал'), ('NL', 'Нидерланды'), ('NI', 'Никарагуа'), ('NE', 'Нигер'), ('NG', 'Нигерия'), ('NU', 'Ниуэ'), ('NO', 'Норвегия'), ('OM', 'Оман'), ('PK', 'Пакистан'), ('PW', 'Палау'), ('PA', 'Панама'), ('PY', 'Парагвай'), ('PE', 'Перу'), ('PH', 'Филиппины'), ('PN', 'Питкэрн'), ('PL', 'Польша'), ('PT', 'Португалия'), ('QA', 'Катар'), ('RE', 'Реюньон'), ('RO', 'Румыния'), ('RU', 'Россия'), ('RW', 'Руанда'), ('WS', 'Самоа'), ('SN', 'Сенегал'), ('RS', 'Сербия'), ('SG', 'Сингапур'), ('SK', 'Словакия'), ('SI', 'Словения'), ('SO', 'Сомали'), ('ES', 'Испания'), ('SD', 'Судан'), ('SR', 'Суринам'), ('SZ', 'Свазиленд'), ('SE', 'Швеция'), ('CH', 'Швейцария'), ('SY', 'Сирия'), ('TW', 'Тайвань'), ('TJ', 'Таджикистан'), ('TZ', 'Танзания'), ('TH', 'Таиланд'), ('TG', 'Того'), ('TK', 'Токелау'), ('TO', 'Тонга'), ('TN', 'Тунис'), ('TR', 'Турция'), ('TM', 'Туркменистан'), ('TV', 'Тувалу'), ('UG', 'Уганда'), ('UA', 'Украина'), ('UY', 'Уругвай'), ('UZ', 'Узбекистан'), ('VU', 'Вануату'), ('VE', 'Венесуэла'), ('VN', 'Вьетнам'), ('YE', 'Йемен'), ('ZM', 'Замбия'), ('ZW', 'Зимбабве'), ('AX', 'Аландские острова'), ('AS', 'Американское Самоа'), ('BS', 'Багамские острова'), ('BM', 'Бермудские острова'), ('BV', 'Остров Буве'), ('KY', 'Каймановы острова'), ('CF', 'Центральноафриканская Республика'), ('CX', 'Остров Рождества'), ('KM', 'Коморские острова'), ('CK', 'Острова Кука'), ('DO', 'Доминиканская Республика'), ('GQ', 'Экваториальная Гвинея'), ('FO', 'Фарерские острова'), ('GF', 'Французская Гвиана'), ('PF', 'Французская Полинезия'), ('VA', 'Святой Престол'), ('IM', 'Остров Мэн'), ('KP', 'Северная Корея'), ('KR', 'Южная Корея'), ('MH', 'Маршалловы острова'), ('NC', 'Новой Каледонии'), ('NZ', 'Новая Зеландия'), ('NF', 'Остров Норфолк'), ('SA', 'Саудовская Аравия'), ('SC', 'Сейшельские острова'), ('SB', 'Соломоновы Острова'), ('ZA', 'Южная Африка'), ('SS', 'Южный Судан'), ('GB', 'Соединенное Королевство'), ('EH', 'Западная Сахара'), ('AG', 'Антигуа и Барбуда'), ('BA', 'Босния и Герцеговина'), ('TF', 'Французские южные территории'), ('MP', 'Северные Марианские острова'), ('TT', 'Тринидад и Тобаго'), ('AE', 'Объединенные Арабские Эмираты'), ('US', 'Соединенные Штаты Америки'), ('WF', 'Уоллис и Футуна'), ('TC', 'Острова Теркс и Кайкос'), ('UM', 'Внешние малые острова США'), ('IO', 'Британская территория в Индийском океане'), ('HM', 'Остров Херд и Острова Макдоналд'), ('GS', 'Южная Георгия и Южные Сандвичевы острова'), ('VG', 'Виргинские Острова (Британские)'), ('VI', 'Виргинские Острова (США)'), ('MF', 'Святого Мартина (Остров, французская часть)'), ('SX', 'Святого Мартина (Остров, нидерландская часть)'), ('SJ', 'Шпицберген и Ян-Майен'), ('FK', 'Фолклендские острова [Мальвинские]'), ('CD', 'Конго (Демократическая Республика)'), ('FM', 'Микронезия (Федеративные Штаты)'), ('CC', 'Кокосовые (Килинг) острова'), ('SH', 'Святой Елены, Вознесения и Тристан-да-Кунья (Острова)'), ('SM', 'Сан - Марино'), ('PS', 'Палестина, Государство'), ('BQ', 'Бонайре, Синт-Эстатиус и Саба'), ('BF', 'Буркина-Фасо'), ('CV', 'Кабо-Верде'), ('CR', 'Коста-Рика'), ('GW', 'Гвинея-Бисау'), ('PR', 'Пуэрто-Рико'), ('BL', 'Сен-Бартельми'), ('LC', 'Сент-Люсия'), ('SL', 'Сьерра-Леоне'), ('LK', 'Шри-Ланка'), ('TL', 'Тимор-Лесте'), ('PG', 'Папуа-Новая Гвинея'), ('KN', 'Сент-Китс и Невис'), ('PM', 'Сен-Пьер и Микелон'), ('VC', 'Сент-Винсент и Гренадины'), ('ST', 'Сан-Томе и Принсипи'), ('CI', "Кот-д'Ивуар"), ('EU', 'European Union')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='price',
            field=django_prices.models.MoneyField(currency='RUB', decimal_places=2, max_digits=12),
        ),
    ]