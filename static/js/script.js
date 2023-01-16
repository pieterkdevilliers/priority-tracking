window.addEventListener('DOMContentLoaded', (event) => {
var actions_page = document.getElementById("on-priority-perc");
if (actions_page != null) {

let on_priority_perc = document.getElementById("on-priority-perc").innerText;
let today_report = document.getElementById("today-report")
if (on_priority_perc < 70) {
    today_report.style.cssText = `
    border: 3px solid red
    `;
        }
else {
    today_report.style.cssText = `
    border: 3px solid green
    `;
};

let on_priority_perc_all_time = document.getElementById("on_priority_perc_all_time").innerText;
let averages_report = document.getElementById("averages-report")
if (on_priority_perc_all_time < 70) {
    averages_report.style.cssText = `
    border: 3px solid red
    `;
        }
else {
    averages_report.style.cssText = `
    border: 3px solid green
    `;
};

}});



    



