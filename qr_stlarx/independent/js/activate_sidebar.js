
// No JQuery
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {draggable: false});
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {accordion: false});
    var elems = document.querySelectorAll('.tabs');
    var instance = M.Tabs.init(elems);
});
