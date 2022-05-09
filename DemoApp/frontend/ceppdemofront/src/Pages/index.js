import React, { useState } from 'react';
import axios from 'axios';

const HomePage = () => {
    let formData = new FormData();
    const [csvFile, setCsvFile] = useState();
    if (csvFile){
        formData.append('path_to_csv', csvFile); 
    }

    const handleChange = (e) => {
        if (e.currentTarget.files) setCsvFile(e.currentTarget.files[0]);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        async function fetchData() {
            const res = await axios.post(
            'http://127.0.0.1:8000/test',
            formData,
            );
            console.log(res.data);
            }

        fetchData();
    };


    return (
        <div className="flex flex-col gap-6 justify-center items-center h-screen">
            <h1> Page Title</h1>
            <form onSubmit={handleSubmit}>
            <input type="file" accept=".csv" onChange={handleChange} />
            <button type="submit" className="bg-blue-500 px-4 py-2 rounded-md font-semibold">fetch</button>
            </form>
        </div>
    );
};

export default HomePage;