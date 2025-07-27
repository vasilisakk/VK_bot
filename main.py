print('Бот запущен')
stop = False

while not stop:
    try:
        import vk_api
        from vk_api.longpoll import VkEventType, VkLongPoll
        import time
        import datetime
        import config
        from yandex_gpt import generate_answer_from_file

        vk = vk_api.VkApi(token=config.token)
        longpoll = VkLongPoll(vk)

        def get_keyboard(path):
            keyboard = open(f"keyboards/{path}.json", "r", encoding="UTF-8").read()
            return keyboard

        def send_msg(user_id, message, keyboard = None):
            vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0, 'keyboard': keyboard})

        def send_hello(user_id):
            keyboard = get_keyboard("main")
            send_msg(user_id, f'Привет, {get_user_name(user_id)}! Я — бот от VK Education Projects.\n'
                              f'Ниже в меню ты можешь посмотреть ответы на часто\n'
                              f'задаваемые вопросы, и если твоего вопроса там нет, я постараюсь на него ответить!',
                     keyboard)

        def what_is_VkEducationProjects(user_id):
            send_msg(user_id, 'VK Education Projects — витрина проектов для студентов. '
                  'Проекты могут быть использованы для выполнения домашних заданий, '
                  'научно-исследовательских, курсовых и дипломных работ.\n'
                  'Доступны задачи по пяти направлениям от AI VK, All Cups,'
                  ' Почты Mail, VK Education, VK Рекламы, VK Play, VK Tech'
                  ' и ВКонтакте: анализ данных и машинное обучение, '
                  'разработка, информационная безопасность, креативные индустрии и продукт.')

        def get_user_name(user_id):
            user_name = vk.method('users.get', {'user_ids': user_id, 'fields': 'first_name'})
            user_name = user_name[0]['first_name']
            return user_name

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                msg = event.text.lower()
                user_id = event.user_id
                if msg == 'начать':
                    send_hello(user_id)
                elif msg == 'что такое vk education projects?':
                    what_is_VkEducationProjects(user_id)
                elif msg == 'ответы на частые вопросы':
                    faq_keyboard = get_keyboard("faq")
                    send_msg(user_id, "Выберите интересующий вас вопрос:", faq_keyboard)
                elif msg == 'кто может участвовать в программе?':
                    send_msg(user_id, 'Школьники, студенты бакалавриата, специалитета,'
                                      ' магистратуры и аспирантуры всех вузов России, '
                                      'а также научные руководители и преподаватели, '
                                      'которые хотят использовать кейсы VK в обучении студентов.', get_keyboard("faq"))
                elif msg == 'можно ли выбрать несколько задач?':
                    send_msg(user_id, "Да, можно решать неограниченное количество задач.", get_keyboard("faq"))

                elif msg == 'где можно использовать решения задач?':
                    send_msg(user_id, "Задачи от VK можно использовать в практической части выпускных "
                                      "квалификационных, курсовых и научно-исследовательских работ, "
                                      "а также взять за основу домашних заданий.",
                             get_keyboard("faq"))

                elif msg == 'как получить данные для решения задачи?':
                    send_msg(user_id,
                             "Выбери задачу, пройди регистрацию — и тебе откроется доступ к "
                             "материалам, которые понадобятся в процессе работы над задачей.",
                             get_keyboard("faq"))

                elif msg == 'я получу сертификат?':
                    send_msg(user_id,
                             "Если ты выполнишь все условия, описанные в выбранной задаче, "
                             "то сможешь получить сертификат о работе над проектом VK.",
                             get_keyboard("faq"))

                elif msg == 'будут ли ставить оценки?':
                    send_msg(user_id,
                             "Нет, оценки за решения задач не предусмотрены. Однако если ты"
                             " выполнишь требования, описанные в задаче, поделишься с нами результатами"
                             " работы и твоё решение высоко оценят эксперты, мы свяжемся с тобой и "
                             "подготовим рецензию.",
                             get_keyboard("faq"))

                elif msg == 'как формировались задачи?':
                    send_msg(user_id,
                             "Все задачи на витрине — исследовательские и носят "
                             "экспериментальный характер, составлены с учётом актуального бизнес-контекста. "
                             "Задачи сформулированы таким образом, чтобы у участников была возможность "
                             "реализовать свой талант, работая над интересными проектными кейсами.",
                             get_keyboard("faq"))

                elif msg == 'кому я могу задать вопросы?':
                    send_msg(user_id,
                             "Следи за расписанием вебинаров на странице проекта — ты сможешь задать"
                             " вопросы по задаче экспертам VK."
                             "\nЕсли у тебя есть организационные вопросы, задай их на обучающей платформе.",
                             get_keyboard("faq"))

                elif msg == 'я не могу найти подходящую задачу':
                    send_msg(user_id,
                             "В банке задач появляются новые интересные кейсы от департаментов VK, следи за обновлениями.",
                             get_keyboard("faq"))

                elif msg == 'назад':
                    send_hello(user_id)




                else:

                    # Генерация ответа с использованием текста из файла

                    answer = generate_answer_from_file("vkeducation.txt", msg)  # Путь к файлу с данными

                    send_msg(user_id, answer, get_keyboard("main"))


    except Exception as error_msg:
        print(f'Ошибка:\n   {error_msg}')
        time.sleep(15)
        print('Перезапуск')