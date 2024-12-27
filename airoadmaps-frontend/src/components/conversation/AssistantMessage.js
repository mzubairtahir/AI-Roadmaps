



const AssistantMessage  = ({content})=>{

    return <div className="flex justify-start">

     <div className="bg-accent my-4 rounded w-3/4 p-2 sm:w-auto sm:max-w-[60%]">
        {content}
    </div>
    </div>

}

export default AssistantMessage;