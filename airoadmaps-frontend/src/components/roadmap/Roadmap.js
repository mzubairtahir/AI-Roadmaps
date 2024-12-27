import Module from "./Module";
import WhatLearn from "./WhatLearn";

const Roadmap = ({ roadmapData }) => {

    return <>
        <div className="text-sm sm:text-base ">
            <div className="text-center py-2"><h1 className="text-2xl sm:text-3xl">{roadmapData.title}</h1></div>
            <div><p className="py-4">{roadmapData.description}</p></div>
            <div><h2 className="text-lg py-2">What you'll learn?</h2></div>
            <div className="py-2">
                <WhatLearn whatlearnData={roadmapData.learning_outcomes} />
            </div>
            <div><h2 className="text-lg py-2">Prerequisites</h2></div>
            <div>
                {
                    roadmapData.prerequisites.map((element, index) => {
                        return <div key={index} className="flex py-1" >
                            <div>
                                <svg fill="green" width={"20px"} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                                    <path d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z" /></svg>
                            </div>
                            <p className="pl-4">

                                {element}
                            </p>
                        </div>
                    })
                }

            </div>


            <div><h2 className="text-lg py-2">Modules</h2></div>
            <div className="py-2">
                {roadmapData.modules.map((element, index)=>{
                    return <Module key={index} moduleData={element} />

                })}
            </div>
            <div><h2 className="text-lg py-2">Final Project</h2></div>
            <div><p className=" py-2">{roadmapData.project}</p></div>









        </div>
    </>

}

export default Roadmap; 