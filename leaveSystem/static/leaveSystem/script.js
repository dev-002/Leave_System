
function respond(id, is_approved){
    document.querySelectorAll(`.disable-${id}`).forEach(button => {
        button.style.display = "none";
    })
    document.querySelector(`.toggle-${id}`).style.display = "inline";
    fetch(`respond/${id}/${is_approved}`)
        .then(Response=>Response.text())
        .then(text=>{
            msg = "Approved"
            if (is_approved === 0){
                msg = "Rejected"
            }
            document.querySelector(`.toggle-${id}`).style.display = "none";
            document.querySelector(`#id_${id}`).innerHTML = msg;
            console.log(text);
        })
        .catch(error =>{
            console.log(error)
        })
        .finally(()=>{

        }
        );
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.approve').forEach(button => {
        button.onclick = function(){
            respond(this.dataset.id, 1)
        }
    });

    document.querySelectorAll('.reject').forEach(button => {
        button.onclick = function(){
            respond(this.dataset.id, 0)
        }
    });
})
