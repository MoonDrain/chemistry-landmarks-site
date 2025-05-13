document.addEventListener('DOMContentLoaded', function () {

    // --- 1. Получаем доступ к элементам информационных блоков ---
    const infoBlock1Title = document.querySelector('#info-block-1 h2');
    const infoBlock1Text = document.querySelector('#info-block-1 p');
    const infoBlock2Title = document.querySelector('#info-block-2 h3');
    const infoBlock2Text = document.querySelector('#info-block-2 p');

    // --- 2. Данные для наших достопримечательностей ---
    const chemicalLandmarks = [
        {
            lat: 59.9401,
            lng: 30.2780,
            title: "Аптека Пеля (Музей-аптека доктора Пеля)",
            address: "Санкт-Петербург, 7-я линия Васильевского острова, 16–18",
            description: "Историческая аптека и музей с уникальной атмосферой и экспонатами.",
            details: "Знаменита своей Башней Грифонов и старинными интерьерами, хранящими тайны алхимии и фармацевтики."
        },
        {
            lat: 59.9321,
            lng: 30.3475,
            title: "Музей «РетроФармаМед»",
            address: "Санкт-Петербург, Невский проспект, 65",
            description: "Музей истории медицины и фармации с коллекцией старинных инструментов и лекарств.",
            details: "Представлены уникальные экспонаты аптечной посуды, оборудования и медицинских инструментов прошлых веков."
        },
        {
            lat: 59.9341,
            lng: 30.3356,
            title: "Музей гигиены",
            address: "Санкт-Петербург, ул. Итальянская, 25",
            description: "Экспозиции, посвященные здоровью человека, профилактике заболеваний и истории гигиены.",
            details: "Один из старейших медицинских музеев, наглядно демонстрирующий важность здорового образа жизни."
        },
        {
            lat: 59.9392,
            lng: 30.2978,
            title: "Музей-архив Д. И. Менделеева (СПбГУ)",
            address: "Санкт-Петербург, Менделеевская линия, 2 (Здание Двенадцати коллегий, СПбГУ)",
            description: "Мемориальный кабинет-музей великого химика, создателя Периодической системы элементов.",
            details: "Содержит личные вещи, библиотеку, научные труды и приборы Д.И. Менделеева, воссоздает рабочую обстановку ученого."
        },
        {
            lat: 59.9274,
            lng: 30.2854,
            title: "Санкт-Петербургский химико-фармацевтический университет (СПХФУ)",
            address: "Санкт-Петербург, Татарский переулок, 12–14",
            description: "Один из ведущих вузов России в области фармации и химической технологии.",
            details: "Готовит высококвалифицированных специалистов для фармацевтической промышленности и научных исследований."
        }
    ];

    // --- 3. Функция для обновления информационных блоков ---
    function updateInfoPanel(landmark) {
        if (!landmark) { // Если объект landmark не передан (например, массив пуст)
            infoBlock1Title.textContent = "Выберите объект на карте";
            infoBlock1Text.textContent = "Информация о достопримечательности появится здесь.";
            infoBlock2Title.textContent = "Дополнительно";
            infoBlock2Text.textContent = "Детали будут загружены после выбора объекта.";
            return;
        }

        infoBlock1Title.textContent = landmark.title;
        infoBlock1Text.textContent = landmark.address; // Адрес в первом блоке

        infoBlock2Title.textContent = "Описание и детали"; // Заголовок для второго блока
        let detailsContent = landmark.description; // Начинаем с основного описания
        if (landmark.details) {
            detailsContent += ` ${landmark.details}`; // Добавляем более подробные детали
        }
        infoBlock2Text.textContent = detailsContent;
    }

    // --- 4. Инициализация карты ---
    // Координаты центра Санкт-Петербурга и уровень масштабирования
    // (можешь подстроить по своему вкусу, например, зум 14, 15 или 16)
    const map = L.map('map').setView([59.93458, 30.30886], 13);

    // Добавление слоя тайлов (подложки карты) - используем CARTO Positron
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20,
        detectRetina: true // Для четкости на HiDPI экранах
    }).addTo(map);

    /*
    // Альтернатива: Стандартные тайлы OpenStreetMap (если CARTO не нравится)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        detectRetina: true
    }).addTo(map);
    */

    // --- 5. Инициализируем инфо-панель ---
    // Отображаем информацию о первой достопримечательности при загрузке, если массив не пуст
    if (chemicalLandmarks.length > 0) {
        updateInfoPanel(chemicalLandmarks[0]);
    } else {
        // Если массив chemicalLandmarks пуст, показываем плейсхолдеры
        updateInfoPanel(null);
    }

    // --- 6. Добавляем маркеры на карту, используя данные из массива ---
    chemicalLandmarks.forEach(function(landmark) {
        const marker = L.marker([landmark.lat, landmark.lng]).addTo(map);

        // Формируем контент для всплывающего окна (popup) - только заголовок,
        // так как остальная информация будет в инфо-блоках.
        marker.bindPopup(`<b>${landmark.title}</b>`);

        // Добавляем обработчик клика на маркер
        marker.on('click', function() {
            updateInfoPanel(landmark); // Вызываем функцию обновления с данными этого маркера

            // Опционально: центрирование карты на маркере при клике
            // map.setView([landmark.lat, landmark.lng], map.getZoom()); // Мгновенно
            // map.flyTo([landmark.lat, landmark.lng], map.getZoom()); // С плавной анимацией
        });
    });

}); // Конец document.addEventListener('DOMContentLoaded', ...)