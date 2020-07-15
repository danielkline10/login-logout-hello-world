import React, { Component } from "react";
import ReactPlayer from "react-player"
import axiosInstance from "../axiosApi";

class Hello extends Component {
    constructor(props) {
        super(props);
        this.state = {
            message: "",

        };

        this.getMessage = this.getMessage.bind(this)
    }

    async getMessage() {
        try {
            let response = await axiosInstance.get('/hello/');
            const message = response.data.hello;
            const uurl = "https://www.youtube.com/watch?v=EIhwc6uX_uM";
            this.setState({
                message: message,

            });
            return message;
        } catch (error) {
            console.log("Hello error: ", JSON.stringify(error, null, 4));
            // throw error; todo
        }
    }

    componentDidMount() {
        // It's not the most straightforward thing to run an async method in componentDidMount

        // Version 1 - no async: Console.log will output something undefined.
        this.getMessage();
    }

    render() {
        return (
            <div>
                <p>{this.state.message}</p>
                <div>
                    <ReactPlayer
                        url="https://www.youtube.com/watch?v=EIhwc6uX_uM"
                    />
                </div>

            </div>
        )
    }
}

export default Hello;