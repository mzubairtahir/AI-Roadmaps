



const UserMessage = ({ content }) => {


    return <div className="flex justify-end">

        <div className="w-3/4 bg-[#E5E7EB] rounded p-2 text-[#333333] my-4 sm:w-auto  sm:max-w-[50%]" >
            {content}
        </div>
    </div>
}

export default UserMessage;