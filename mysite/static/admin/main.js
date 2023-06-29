document.addEventListener('DOMContentLoaded', function() {
    load_tab('Waiting');
    document.querySelector('#Waiting-tab').addEventListener('click', () => load_tab('Waiting'));
    document.querySelector('#Confirmed-tab').addEventListener('click', () => load_tab('Confirmed'));
    document.querySelector('#Sent-tab').addEventListener('click', () => load_tab('Sent'));
    document.querySelector('#Cancelled-tab').addEventListener('click', () => load_tab('Cancelled'));
  });

function load_tab(tab){
    document.querySelector('#' + `${tab}`+ '-tab-pane').innerHTML = `<h3>${tab.charAt(0).toUpperCase() + tab.slice(1)}:</h3>`;
}

// function AddProduct(){
//     document.querySelector('#content-related').style.display = 'none';
//     const appList =  document.querySelectorAll('#app_list');
//         for (let i = 0; i < appList.length; i++) {
//             appList[i].style.display = 'none';
//         }
//     document.querySelector('#Add-tab-pane').innerHTML = '<h3>Add Product:</h3>';
//     // console.log(document.querySelectorAll('#app_list'))
//     // document.querySelector('#compose-view').style.display = 'block';
// }
// HTMLInputElementObject.addEventListener('input', function (evt) {
//     alert("sss")
// });