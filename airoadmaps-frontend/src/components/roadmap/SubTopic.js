'use client';
import { useState } from "react";

const SubTopic = ({ subtopicData }) => {
    const [collapsed, setCollapsed] = useState(true);


    return <>
        <div className="bg-white text-black px-4 py-2 rounded">
            <div onClick={() => setCollapsed((preCollapsed) => !preCollapsed)} className="cursor-pointer  w-full py-4 flex justify-between items-center">
                <div className="font-bold">{subtopicData.title}</div>
                <div className="pl-2">
                    {
                        collapsed ?
                            <svg fill="black" width={"15px"} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512">
                                <path d="M278.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-160 160c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L210.7 256 73.4 118.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l160 160z" /></svg>
                            :

                            <svg fill="black" width={"15px"} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                                <path d="M201.4 374.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 306.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z" /></svg>

                    }
                </div>
            </div>
            {
                collapsed ? null :
                    <div>
                        <div className="py-2">{subtopicData.description}</div>
                        <div className="flex items-center">

                            <div>
                                <svg width={"30px"} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                                    <path fill="#ff0000" d="M549.7 124.1c-6.3-23.7-24.8-42.3-48.3-48.6C458.8 64 288 64 288 64S117.2 64 74.6 75.5c-23.5 6.3-42 24.9-48.3 48.6-11.4 42.9-11.4 132.3-11.4 132.3s0 89.4 11.4 132.3c6.3 23.7 24.8 41.5 48.3 47.8C117.2 448 288 448 288 448s170.8 0 213.4-11.5c23.5-6.3 42-24.2 48.3-47.8 11.4-42.9 11.4-132.3 11.4-132.3s0-89.4-11.4-132.3zm-317.5 213.5V175.2l142.7 81.2-142.7 81.2z" /></svg>
                            </div>
                            <a target="_blank" href={`https://www.youtube.com/results?search_query=${subtopicData.query}`} className="rounded w-auto bg-accent  px-2 py-1 text-white ml-2">
                                {subtopicData.query}
                            </a>

                        </div>
                        <div><h2 className="text-lg">Activities</h2></div>


                        <div className="py-4">
                            {subtopicData.activities.map((element, index) => {
                                return <div className="flex" >
                                    <div>
                                        <svg fill="green" width={"20px"} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                                            <path d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z" /></svg>
                                    </div>
                                    <p className="pl-4 ">
                                        {element}
                                    </p>
                                </div>
                            })}



                        </div>





                    </div>
            }
        </div>
    </>

}

export default SubTopic;