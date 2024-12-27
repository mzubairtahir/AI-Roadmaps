'use client';

import { useState } from "react";
import SubTopic from "./SubTopic";

const Module = ({ moduleData }) => {
    const [collapsed, setCollapsed] = useState(true);

    return <>
        <div className="bg-white text-black px-4 my-2 py-2 rounded">
            <div onClick={() => setCollapsed((preCollapsed) => !preCollapsed)} className="cursor-pointer  w-full py-4 flex justify-between items-center">
                <div className="font-bold">{moduleData.title}</div>
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
                        <div className="py-2">{moduleData.description}</div>
                        <div><h2 className="text-lg">Subtopics</h2></div>
                        <div className="py-2">
                            {moduleData.subtopics.map((element,  index) => {
                                return <SubTopic key={index} subtopicData={element} />

                            })}


                        </div>
                        <div><h2 className="text-lg py-2">Module Project</h2></div>
                        <div className="px-4"><p>{moduleData.project}</p></div>
                        <div><h2 className="text-lg py-2">Objectives</h2></div>
                        <div className="px-4">
                            {moduleData.objectives.map((element,index) => {
                                return <div key={index} className="flex" >
                                    <div>
                                        <svg fill="green" width={"20px"} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                                            <path d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z" /></svg>
                                    </div>
                                    <p className="pl-4">

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

export default Module;