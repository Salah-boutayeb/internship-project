
const getProgress=(params)=>{
  
    $.ajax({
        type: 'GET',
        url:`/formateur/stagiaire_progress/${params}`,
        success: (response)=>{
          let xValues =[]
          let yValues =[]
            const progress = response.data.progress
            console.log(progress);
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



