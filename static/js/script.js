// Determine if the loaded page is the Actions page.
// If true, then determine if the Today and Average On-Priority Percentage
// is above or below 70% and set border colour accordingly.

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

// Sets and holds the action-date query for filtered-actions
// in order to reload the page with the same query

window.addEventListener('DOMContentLoaded', (event) => {
var filtered_actions_page = document.getElementById("relist-icon");
if (filtered_actions_page != null) {

    console.log(window.location);
    relistQuery = window.location.search;
    const urlParams = new URLSearchParams(relistQuery);
    const relistParam = urlParams.get('action_date');
    document.cookie = 'action_date=' + relistParam;
    console.log(relistParam);
    console.log(document.cookie);
}});  

// Resets the action_date query when a new query is started

document.getElementById("get-filtered-actions").addEventListener("click", resetQuery);

function resetQuery(){
    console.log("resetQuery Function Called");
    console.log(window.location);
    relistQuery = window.location.search;
    const urlParams = new URLSearchParams(relistQuery);
    const relistParam = urlParams.get('action_date');
    document.cookie = "action_date=; expires=Thu, 02 Jan 1970 00:00:01 GMT;"
    console.log(relistParam);
    console.log(document.cookie);
};
    