
// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'dark-theme') {
        setTheme('light-theme');
    } else {
        setTheme('dark-theme');
    }
}

if (localStorage.getItem('theme') === 'dark-theme') {
    setTheme('dark-theme');
    document.getElementById('slider').checked = false;
} else {
    setTheme('light-theme');
    document.getElementById('slider').checked = true;
}

// Immediately invoked function to set the theme on initial load
// (function () {

//     if (localStorage.getItem('theme') === 'dark-theme') {
//         setTheme('dark-theme');
//         document.getElementById('slider').checked = false;
//     } else {
//         setTheme('light-theme');
//         document.getElementById('slider').checked = true;
//     }
// })();


// function addFields() {
//     // Number of inputs to create
//     var number = document.getElementById("member").value;
//     // Container <div> where dynamic content will be placed
//     var container1 = document.getElementById("container1");
//     var container2 = document.getElementById("container2");
//     var container3 = document.getElementById("container3");
//     // Clear previous contents of the container
//     while (container1.hasChildNodes()) {
//         container1.removeChild(container1.lastChild);
//     }
//     while (container2.hasChildNodes()) {
//         container2.removeChild(container2.lastChild);
//     }
//     while (container3.hasChildNodes()) {
//         container3.removeChild(container3.lastChild);
//     }
//     for (i = 0; i < number; i++) {
//         // Append a node with a random text
//         //                container.appendChild(document.createTextNode((i+1)));
//         // Create an <input> element, set its type and name attributes

//         var price = document.createElement("input");
//         price.type = "number";
//         price.name = "price" + i;

//         var share = document.createElement("input");
//         share.type = "number";
//         share.name = "share" + i;


//         var fees = document.createElement("input");
//         fees.type = "number";
//         fees.name = "fees" + i;

//         container1.appendChild(price);
//         container2.appendChild(share);
//         container3.appendChild(fees);

//         // Append a line break
//         container.appendChild(document.createElement("br"));
//     }
// }