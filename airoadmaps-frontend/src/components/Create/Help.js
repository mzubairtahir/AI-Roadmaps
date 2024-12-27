import CloseIcon from "../Svg/CloseIcon";



export default function Help({ closeHelp }) {

    return <>
        <div class="fixed overflow-auto z-20  w-full md:w-2/5 text-black p-4  top-0 bottom-0 bg-[var(--foreground)]">
            <div className="flex w-full">
                <h2 className="w-9/12 text-center" >Help</h2>
                <div className="w-3/12 flex justify-end">
                    <button onClick={closeHelp} className=" w-8 h-8 rounded-full flex justify-center items-center">
                        <CloseIcon className="w-4" fill="white" />
                    </button>
                </div>
            </div>
            <div className="my-6">

                <p className="text-xl font-medium">
                    Use the App
                </p>
                <p>
                    You can create personalized learning roadmaps for various technologies using our AI agent by simply sharing some information about yourself. Provide a few details, and the agent will generate a customized roadmap for you.
                </p>
                <ul className="list-inside py-3 text-base list-disc">
                    <li className="mb-"> <strong>Current knowledge level:</strong> Beginner, Intermediate, Expert</li>
                    <li className="mb-"> <strong>Goals:</strong> For example, building projects or job readiness</li>
                    <li className="mb-"> <strong>Interests:</strong> Such as languages or frameworks like Python and Django</li>
                </ul>

            </div>

        </div>
    </>
}