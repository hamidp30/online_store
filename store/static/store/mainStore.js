function FuncQuantity(value){
    let inputprice = document.querySelector('#inputprice').textContent;
    let price = inputprice.slice(2);
    let total = value*price;
    document.querySelector('#total').textContent = total.toFixed(2);
}

function buy(id){
let totalPrice = document.querySelector('#total').textContent;
let quantity = document.querySelector('#Quantity').value;
let remains = document.querySelector('#Remains').textContent - quantity;
fetch('/neworder',{
    method: 'POST',
    body: JSON.stringify ({
        productid: id,
        productprice: totalPrice,
        productqty: quantity,
        Remains: remains
      })        
  })
  .then(response => response.json())
  .then(result => {
    if(result.error){
      console.log(result.error);
    }else if(result.message){
        alert(result.message);
        window.location.href = '../orders';
    }
  });
//  console.log(Remains)

}

function plogin(){
  alert("pless login! Buy after Login");
}