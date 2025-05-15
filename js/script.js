document.addEventListener('DOMContentLoaded', function () {

    // --- Получаем ссылки на элементы, с которыми будем работать ---
    const infoBlock1Title = document.querySelector('#info-block-1 h2');
    const infoBlock1Text = document.querySelector('#info-block-1 p');
    const infoBlock2Title = document.querySelector('#info-block-2 h3');
    const infoBlock2Text = document.querySelector('#info-block-2 p');
    const landmarkPhoto = document.querySelector('#landmark-photo');
    const pageBodyColumns = document.querySelector('.page-body-columns');

    // --- Данные для наших достопримечательностей ---
    // С вашими последними правками для Аптеки Пеля и координатами СПХФУ
    const chemicalLandmarks = [
        {
            name: "Аптека Пеля (первая аптека СПб + лаборатория)",
            lat: 59.9401,
            lng: 30.2780,
            address: "📍 Адрес: 7-я линия В.О., 16–18",
            founded: "⏳ Основан: 1720 – н.в.",
            status: null,
            exposition: "💊 Экспозиция:@@BREAK@@- Старейшая аптека города, основана по указу Петра I.@@BREAK@@- В XIX веке принадлежала семье Пелей.@@BREAK@@- Сохранилась алхимическая башня-лаборатория.",
            interesting: "🧪 Интересное:@@BREAK@@- Здесь изготавливали лекарства для императорской семьи, а в башне проводили химические опыты.@@BREAK@@- В башне якобы хранился «философский камень» – на самом деле там находилась первая в России лаборатория по синтезу йода и брома.",
            imageUrl: "images\\aptpel.jpg" // Локальный путь (нужен относительный для веба)
        },
        {
            name: "Музей истории медицины и фармации",
            lat: 59.9321, lng: 30.3475,
            address: "📍 Адрес: ул. Введенского канала, 6А", founded: "⏳ Основан: 2019 год",
            status: "🏛 Статус: Частный музей при фармкомпании",
            exposition: "💊 Экспозиция:@@BREAK@@- Аптечные весы XVIII–XX вв.@@BREAK@@- Подлинные рецепты с автографами Боткина и Павлова@@BREAK@@- Реконструкция кабинета провизора",
            interesting: "🧪 Интересное:@@BREAK@@- Единственный в России «Яд-шкаф» с замком 1843 года@@BREAK@@- Интерактивная зона с запахами исторических лекарств",
            imageUrl: "images\\mednfarm.jpg" // Локальный путь
        },
        {
            name: "Музей гигиены",
            lat: 59.9341, lng: 30.3356,
            address: "📍 Адрес: ул. Итальянская, 25", founded: "⏳ Основан: 1919 год",
            status: "🏛 Статус: Научно-просветительский центр",
            exposition: "💊 Экспозиция:@@BREAK@@- «Аптека гигиены» 1920-х с уникальными санпросветплакатами@@BREAK@@- Коллекция венерических симуляторов для обучения врачей",
            interesting: "🧪 Интересное:@@BREAK@@- Хранится чемоданчик «Чумного доктора» 1897 года@@BREAK@@- Есть образцы советских презервативов 1930-х",
            imageUrl: "images\\ggen.jpg" // Локальный путь
        },
        {
            name: "Музей при СПбГУ (Медицинский факультет)",
            lat: 59.9392, lng: 30.2978,
            address: "📍 Адрес: Университетская наб., 7–9", founded: "⏳ Основан: 1822 год",
            status: "🏛 Статус: Ведомственный музей",
            exposition: "💊 Экспозиция:@@BREAK@@- Первая в России учебная аптека (1826)@@BREAK@@- Гербарий лекарственных растений Палласа@@BREAK@@- Восковая модель «Человек-аптека» (1830)",
            interesting: "🧪 Интересное:@@BREAK@@- Здесь Менделеев проводил опыты с лекарственными растворами@@BREAK@@- Сохранился «Рецептурный журнал» с пометками студентов",
            imageUrl: "images\\spbgu2.jpg" // Локальный путь
        },
        {
            name: "СПХФУ (Санкт-Петербургский химико-фармацевтический университет)",
            lat: 59.9709, // Координаты СПХФУ из Шага 20
            lng: 30.3105, // Координаты СПХФУ из Шага 20
            address: "📍 Адрес: ул. Профессора Попова, 14", founded: "⏳ Основан: 1919 год",
            status: "🏛 Статус: Действующий вуз с музеем",
            exposition: "💊 Экспозиция:@@BREAK@@- Аптечная утварь 1920–1950-х@@BREAK@@- Первая советская машина для производства таблеток@@BREAK@@- Дипломы выпускников царского периода",
            interesting: "🧪 Интересное:@@BREAK@@- В подвалах сохранился бункер для хранения опия (ныне лаборатория)",
            imageUrl: "images\\sphfu.png" // Локальный путь
        }
    ];

    // --- Функция для обновления информационных блоков и фото (Без изменений) ---
    function updateInfoPanel(landmark) {
        if (!landmark) {
            infoBlock1Title.textContent = "Выберите объект на карте";
            infoBlock1Text.innerHTML = "Информация о достопримечательности появится здесь.";
            infoBlock2Title.textContent = "Подробности";
            infoBlock2Text.innerHTML = "Подробная информация будет загружена после выбора объекта.";
            landmarkPhoto.src = '';
            landmarkPhoto.alt = 'Фотография недоступна';
            landmarkPhoto.style.display = 'none';
            return;
        }

        infoBlock1Title.textContent = landmark.name;

        let info1Content = '';
        if (landmark.address) info1Content += landmark.address.replace(/@@BREAK@@/g, '<br>') + '<br>';
        if (landmark.founded) info1Content += landmark.founded.replace(/@@BREAK@@/g, '<br>') + '<br>';
        if (landmark.status) info1Content += landmark.status.replace(/@@BREAK@@/g, '<br>');

        infoBlock1Text.innerHTML = info1Content;

        infoBlock2Title.textContent = "Подробности";

        let info2Content = '';
        if (landmark.exposition) {
            info2Content += landmark.exposition.replace(/@@BREAK@@/g, '<br>');
        }
        if (landmark.exposition && landmark.interesting) {
            info2Content += '<br><br>';
        }
        if (landmark.interesting) {
            info2Content += landmark.interesting.replace(/@@BREAK@@/g, '<br>');
        }

        info2Content = info2Content.replace(/<br>+/g, '<br>').replace(/<br>$/, '');
        infoBlock2Text.innerHTML = info2Content;

         if (landmark.imageUrl) {
             landmarkPhoto.src = landmark.imageUrl;
             landmarkPhoto.alt = landmark.name;
             landmarkPhoto.style.display = 'block';
         } else {
             landmarkPhoto.src = '';
             landmarkPhoto.alt = 'Фотография недоступна';
             landmarkPhoto.style.display = 'none';
         }
    }

    // --- Функции для показа/скрытия панели (Без изменений) ---
    function showInfoPanel() {
        if (!pageBodyColumns.classList.contains('show-info')) {
            pageBodyColumns.classList.add('show-info');
            setTimeout(function() {
                 map.invalidateSize();
            }, 500);
        }
    }

    function hideInfoPanel() {
        if (pageBodyColumns.classList.contains('show-info')) {
            pageBodyColumns.classList.remove('show-info');
            updateInfoPanel(null);
             setTimeout(function() {
                 map.invalidateSize();
             }, 500);
         }
    }


    // --- Инициализация карты (Без изменений) ---
    const map = L.map('map', { zoomControl: true });

    // --- Добавление слоя тайлов (подложки карты) - CARTO Positron Light (Без изменений) ---
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20,
        detectRetina: true
    }).addTo(map);


    // --- !!! УДАЛЕНА СЕКЦИЯ СОЗДАНИЯ КАСТОМНОГО СТИЛЯ МЕТКИ !!! ---


    // --- Обработчик клика на карте для скрытия панели (Без изменений) ---
    map.on('click', function(e) {
        hideInfoPanel();
    });


    // --- Добавляем маркеры на карту (Теперь стандартные L.marker) ---
    chemicalLandmarks.forEach(function(landmark) {
        // Создаем стандартный маркер Leaflet (Без изменений)
        const marker = L.marker([landmark.lat, landmark.lng]).addTo(map);

        // Привязываем всплывающее окно (popup) с НОВЫМ НАЗВАНИЕМ (Без изменений)
        let popupContent = `<b>${landmark.name}</b>`;
        marker.bindPopup(popupContent, { autoClose: false, closeOnClick: false });

        // Открываем/закрываем попап при наведении (Без изменений)
        marker.on('mouseover', function() {
            marker.openPopup();
        });
        marker.on('mouseout', function() {
            marker.closePopup();
        });

        // Обработчик КЛИКА на маркер (Без изменений)
        marker.on('click', function() {
            marker.closePopup();

            updateInfoPanel(landmark); // Обновляем содержимое панели
            showInfoPanel(); // Показываем панель

            // Центрируем карту на маркере при клике (Без изменений)
            map.flyTo([landmark.lat, landmark.lng], map.getZoom(), { duration: 0.8 });
        });
    });


    // --- Автоматически подгоняем карту под все маркеры при загрузке (Без изменений) ---
    const landmarkPoints = chemicalLandmarks.map(function(landmark) {
        return [landmark.lat, landmark.lng];
    });

    if (landmarkPoints.length > 0) {
        const bounds = L.latLngBounds(landmarkPoints);
        map.fitBounds(bounds, { padding: [50, 50] });
    }


    // --- Изначальное состояние: Скрываем панель при загрузке страницы (Без изменений) ---
    hideInfoPanel();


}); // Конец document.addEventListener('DOMContentLoaded', ...)