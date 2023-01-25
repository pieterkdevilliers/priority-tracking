// Determine if the loaded page is the Actions page.
// If true, then determine if the Today and Average On-Priority Percentage
// is above or below 70% and set border colour accordingly.
window.addEventListener('DOMContentLoaded', (event) => {
    var actions_page = document.getElementById("on-priority-perc");
    if (actions_page !== null) {

        var on_priority_perc = document.getElementById(
            "on-priority-perc").innerText;
        var today_report = document.getElementById("today-report");
        if (on_priority_perc < 70) {
            today_report.style.cssText = `
            border: 3px solid red
            `;
                }
        else {
            today_report.style.cssText = `
            border: 3px solid green
            `;
}

var on_priority_perc_all_time = document.getElementById(
    "on_priority_perc_all_time").innerText;
var averages_report = document.getElementById("averages-report");
if (on_priority_perc_all_time < 70) {
    averages_report.style.cssText = `
    border: 3px solid red
    `;
        }
else {
    averages_report.style.cssText = `
    border: 3px solid green
    `;
}

}});

// Sets and holds the action-date query for filtered-actions
// in order to reload the page with the same query
window.addEventListener('DOMContentLoaded', (event) => {
    var undo_filtered_action = document.getElementById(
        "undo-filtered-action");
    var complete_filtered_action = document.getElementById(
        "complete-filtered-action");
    var relist_filtered_action = document.getElementById(
        "relist-filtered-action");
    var filtered_actions_page = document.getElementById(
        "filtered-action-page");
    if (filtered_actions_page != null) {
        if(undo_filtered_action != null || relist_filtered_action != null) {
            relistQuery = window.location.search;
            const urlParams = new URLSearchParams(relistQuery);
            const relistParam = urlParams.get('action_date');
            document.cookie = 'action_date=' + relistParam;
        } else if
            (undo_filtered_action == null && relist_filtered_action == null) {
                lastQuery = retrieveLastQuery()
                if (lastQuery != null) {
                    window.location.href = "?action_date=" + lastQuery;
                }
            } else 
            relistQuery = window.location.search;
            const urlParams = new URLSearchParams(relistQuery);
            const relistParam = urlParams.get('action_date');
            document.cookie = 'action_date=' + relistParam;
    }});

// Resets the action_date query when a new query is started
window.addEventListener('DOMContentLoaded', (event) => {
document.getElementById(
    "get-filtered-actions").addEventListener("click", resetQuery);

    function resetQuery() {
        document.cookie = "action_date=; expires=Thu, 02 Jan 1970 00:00:01 GMT;";
    }
});

// Retrieves the lates action_date value from cookies
function retrieveLastQuery() {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${"action_date"}=`);
    if (parts.length == 2){
        return parts.pop().split(';').shift();
    }
}

// 2 second timer to remove alerts after display
setTimeout(function(){
    if ($('#message').length > 0) {
        $('#message').remove();
    }
    }, 2000);