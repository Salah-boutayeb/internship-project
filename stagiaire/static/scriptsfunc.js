const box =document.getElementById('box')
const boxTacheTitle =document.getElementById('box-tache-title')
let axe=document.getElementById('sendTaches')
let count=0
let counttache=0
console.log('shit');
function getAxe(params) {
    axe.value=params
    console.log(axe.value);
}

/* ajouter supprimer axe */ 
function addAxe() {   
    count++
   box.insertAdjacentHTML("beforeend",`
    <div class="row " id="row${count}">
        <div class="input-field col s6">
            <input  type="text" id="axe${count}" class="axe${count}" name="axe${count}">
            <label class="active" for="axe${count}">AXE${count}</label>
        </div>
    </div>
    `)
    
}
function removeAxe() {
    document.getElementById(`row${count}`).remove()
    count--
    
}
function addtache () {   
    counttache++
   boxTacheTitle.insertAdjacentHTML("beforeend",`
    <div class="row " id="tache${counttache}">
        <div class="input-field col s12">
            <textarea  type="textarea" id="axe${counttache}" class="tache materialize-textarea" name="tache${counttache}"></textarea>
            <label class="active" for="tache${counttache}">tache${counttache}</label>
        </div>
        
    </div>
    `)
    
}
function removetache() {
    document.getElementById(`tache${counttache}`).remove()
    counttache--
    
}

var xValues = ["DONE","not DONE"];
var yValues = [20,80];
var barColors = [
  
  "#29b6f6",
  "#78909c"
];

new Chart("myChart", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "my progress"
    }
  }
});


