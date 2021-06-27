const box =document.getElementById('box')
const boxTacheTitle =document.getElementById('box-tache-title')
let axe=document.getElementById('sendTaches')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
let count=0
let counttache=0

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
const getProgress=()=>{
  var button=document.getElementById('upload')
    $.ajax({
        type: 'GET',
        url:`/stagiaire/my_progress`,
        success: (response)=>{
          let xValues =[]
          let yValues =[]
            const progress = response.data.progress
            if (response.data.done!=100) {
              
              
              button.disabled = true
            }
            else{
              button.disabled = false
            }
            progress.forEach(element => {

              xValues.push(Object.keys(element))
              yValues.push(Object.values(element))
              
            });
               new Chart("myChart", {
              type: "doughnut",
              data: {
                labels: xValues,
                datasets: [{
                  backgroundColor:  [
                    "#29b6f6",
                    "#78909c"
                  ],
                  data: yValues
                }]
              },
              options: {
                responsive: true,
                
                title: {
                  display: true,
                  text: "my progress"
                }
              }
            }) 
            xValues =[]
            yValues =[]
          },
        error: (error)=>{
            console.error(error);
        },
    })
}

const validate=(params)=>{
  $.ajax({
      type: 'POST',
      url:`/stagiaire/my_progress/${params}`,
      data:{
        'csrfmiddlewaretoken':csrf[0].value,
    },
      success: (response)=>{
        getProgress()

        
        },
      error: (error)=>{
          console.error(error);
      },
  })
}
getProgress()





const delete_tache = (params)=>{
  $.ajax({
      type: 'POST',
      url:`/stagiaire/delete_tache/${params}`,
      data:{
        'csrfmiddlewaretoken':csrf[0].value,
    },
      success: (response)=>{
        
        document.getElementById('list'+params).remove()
        getProgress()
        },
      error: (error)=>{
        console.error(error);
      },
  })
}

const delete_axe = (params)=>{
  $.ajax({
      type: 'POST',
      url:`/stagiaire/delete_axe/${params}`,
      data:{
        'csrfmiddlewaretoken':csrf[0].value,
    },
      success: (response)=>{
        document.getElementById('axe'+params).remove()
        getProgress()
        },
      error: (error)=>{
          console.error(error);
      },
  })
}