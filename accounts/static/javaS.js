console.log('rrrrrrrrrrrr');
const getProgress=()=>{
  
    $.ajax({
        type: 'GET',
        url:`/stagiaire/my_progress`,
        success: (response)=>{
          let xValues =[]
          let yValues =[]
            const progress = response.data.progress
            
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
                  text: "Progress"
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
getProgress()