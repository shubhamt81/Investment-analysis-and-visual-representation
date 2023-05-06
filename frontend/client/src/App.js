import React, { useState, useEffect } from "react"
// import axios from "axios";
// import "./App.css"

function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({})

   useEffect(()=>{
        fetch("http://localhost:5000/funds").then(
            response=>response.json()
        ).then(
            data=>{
                setdata(data)
                console.log(data)
            }

        )

   },[])

    // const getData = async () => {
    //     try {
    //         var res = await axios.get('/funds');
    //         console.log(res.data);
    //     }
    //     catch(err) {
    //         console.error(err);
    //     }
    // };
  
    // getData();
    return (
        <div>
            cat
        </div>
    )
}
  
export default App
