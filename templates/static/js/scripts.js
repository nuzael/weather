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

setInterval(updateDatetime, 1000);
setDayOfTheWeek();
updateDatetime();