//
//  ContentViewModel.swift
//  SmartHome
//
//  Created by Developer on 18.03.2023.
//

import Foundation
import Alamofire

class ContentViewModel {
    
    private var baseUrl = URL(string: "http://raspberrypi:8000")!
    
    func toggleRelay() {
        sendRequest(path: "toggle/relay")
    }
    
    func toggleLed() {
        sendRequest(path: "toggle/led")
    }
    
    func ledRed() {
        sendRequest(path: "led/red")
    }
    
    func ledGreen() {
        sendRequest(path: "led/green")
    }
    
    func ledBlue() {
        sendRequest(path: "led/blue")
    }
    
    private func sendRequest(path: String) {
        Task {
            do {
                AF.sessionConfiguration.timeoutIntervalForRequest = 5
                let url = baseUrl.appendingPathComponent(path)
                let response = try await AF.request(url, method: .get).serializingString().value
                print(response)
            } catch {
                print(error)
            }
        }
    }
    
}
