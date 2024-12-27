
import AssistantMessage from "./AssistantMessage"
import UserMessage from "./UserMessage"




const Conversation = ({messages})=>{
    
    return <>
    <div>
        <div className="px-2 sm:px-6 mb-16">

        {messages.map((item, index )=> (
            item.role==="user"?<UserMessage content={item.content}/>:<AssistantMessage content={item.content}/>
                

        ) 
        )}
        {/* Lorem ipsum dolor sit, amet consectetur adipisicing elit. Praesentium, voluptates? */}
        </div>

    </div>
    </>
}


export default Conversation