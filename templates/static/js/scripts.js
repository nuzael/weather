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

setInterval(updateDatetime, 1000);
updateDatetime();