//
//  ContentView.swift
//  SmartHome
//
//  Created by Developer on 18.03.2023.
//

import SwiftUI

struct ContentView: View {
    
    var model = ContentViewModel()
    
    var body: some View {
        VStack(alignment: .leading) {
            
            Text("SmartHome")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Button(action: model.toggleRelay) {
                label(text: "Toggle relay", image: "power")
            }
            
            Button(action: model.toggleLed) {
                label(text: "Toggle led", image: "power")
            }
            
            Divider()
            
            Button(action: model.ledRed) {
                label(text: "Led red", image: "eyedropper")
                    .accentColor(Color.red)
            }
            
            Button(action: model.ledGreen) {
                label(text: "Led green", image: "eyedropper.halffull")
                    .accentColor(Color.green)
            }
            
            Button(action: model.ledBlue) {
                label(text: "Led blue", image: "eyedropper.full")
                    .accentColor(Color.blue)
            }
            
            Spacer()
        }
        .padding()
    }
    
    @ViewBuilder
    func label(text: String, image: String) -> some View {
        Label(text, systemImage: image)
            .frame(maxWidth: .infinity)
            .padding()
            .background(
                RoundedRectangle(cornerRadius: 15)
                    .stroke()
                    .foregroundColor(Color.gray)
            )
            .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
