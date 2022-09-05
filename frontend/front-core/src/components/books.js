import React from 'react'
import axios from "axios";
import { useEffect, useState } from 'react';



const API = "http://127.0.0.1:8000/graphql/" 

function getAPIdata(){
  const body = {
    query: ` {
        books {
          pk
          title
        }
    }`
}
  return axios.post(API, body).then((response) => {
    // console.log(response.data.data.books)
    return response.data.data.books})
}


function Books() {

  const [books, setBooks] = useState([]);

  useEffect(()=>{
    let mounted = true;
    getAPIdata().then((items) => {
      if (mounted){
        setBooks(items);
      }
    });

    return () => (mounted = false);

  }, []);


  return (
    <div 
    >These books are from the ariadne API
    <ul style={{width: "400px", textAlign: "left", marginLeft: "50px"}} >
    {
        books.map(item => {
            return <li key={item.pk} >{item.title}</li>
        })
    }
    </ul>
    </div>
    
    
  )
}

export default Books