[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803321&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

 Kamish Charniya and Walter Silbert 

***

## Project Description

 This project will incorporate crypto prices in real time and allow the user to use a button to update the prices in real time. We will possibly use rest API's from cryptocurreny sites that display real time price like Coinbase or Blockchain.com.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. GUI usage
2. Button usage
3. Image usage
4. Pygame usage
5. << Feature 5 >>

### Classes

- << You should have a list of each of your classes with a description >>
CryptoCurrency:

Represents a cryptocurrency entity, storing information such as name, symbol, price, market capitalization, and 24-hour trading volume.
Methods include update_price, get_market_cap, and get_volume_24h for modifying and accessing specific data attributes of a cryptocurrency.

CryptoTracker:

Manages a list of CryptoCurrency instances, initializes them, and fetches cryptocurrency prices from an API.
Controls the tkinter-based display, updating it with fetched cryptocurrency information at regular intervals.
Includes methods like initialize_currencies, fetch_crypto_prices, create_display, update_display, and continuous_update_and_display.

CryptoTrackerController:

Acts as a higher-level controller managing the interaction between the CryptoTracker and the tkinter display.
Initializes a tkinter window and the CryptoTracker, starting the continuous display updates.

All of these are our separate classes at the moment from whihc our project is made upon.
## ATP


