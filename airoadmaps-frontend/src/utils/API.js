

const API = {

    async createRoadmap(messages) {
        try {
            const response = await fetch("/api/chat", {
                method: "post",
                headers: {
                    "Content-Type": "Application/Json"
                },
                body:JSON.stringify({"messages":messages})
            })


            return response;



        }
        catch (error) {
            return

        }

    },
    async login(access_token){
        const response = await fetch("/api/auth/login",{
            method:"post",  
            headers: {
                "Content-Type": "Application/Json"
            },
            body:JSON.stringify({
                "access_token": access_token
              })
        })

        return response;


    },
    async getRoadmap(id){
        const response = await fetch(`/api/roadmap/${id}`,{
            credentials: 'include'
        })
        

        return response;


    }
}

export default API;