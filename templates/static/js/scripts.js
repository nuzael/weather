function updateDatetime() {
    var currentDatetime = new Date();
    var datetimeFormat = {
        weekday: "long",
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
    };

    var formattedTime = currentDatetime.toLocaleTimeString("pt-BR", datetimeFormat);

    var spanDatetime = document.getElementById("datetime");
    spanDatetime.textContent = formattedTime;
}

function setDayOfTheWeek() {
    const currentDate = new Date();
    const currentDayIndex = currentDate.getDay();


    const daysOfWeek = [
        "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"
    ];

    const orderedDaysOfWeek = [
        ...daysOfWeek.slice(currentDayIndex),
        ...daysOfWeek.slice(0, currentDayIndex)
    ];

    const forecastTitleElements = document.querySelectorAll('#forecast-title');

    forecastTitleElements.forEach((element, index) => {
        element.textContent = orderedDaysOfWeek[index+1];
    });
}

function setDayIcon() {
    const currentDayIconElement = document.querySelector('#main-weather-icon');
    var posIndex = currentDayIconElement.src.indexOf("@") - 1;

    const dayIconElements = document.querySelectorAll('#day-icon');

    dayIconElements.forEach((element) => {
        if (currentDayIconElement.src[posIndex] == "d") {
            element.textContent = "https://openweathermap.org/img/wn/{{ day.icon }}d@2x.png"
        }
        else {
            element.textContent = "https://openweathermap.org/img/wn/{{ day.icon }}n@2x.png"
        }
    });
}

setInterval(updateDatetime, 1000);
setDayOfTheWeek();
setDayIcon();
updateDatetime();