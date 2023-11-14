# README (中文版)

## 交換學校資訊整合程式

### 簡介

此程式用於整合國立臺灣科技大學（NTUST）112-2學期（2024春季）的交換學校名單與該校的QS排名，並將結果輸出為一份Excel檔案。程式透過網路爬蟲的方式，從臺灣科技大學的網站和QS排名網站獲取所需資訊。

### 使用方式

1. 安裝相依套件：

   ```bash
   pip install pandas requests beautifulsoup4
   ```

2. 執行程式：

   ```bash
   python exchange-program_NTUST.py
   ```

3. 檢查輸出：

   程式執行完畢後，將在同一目錄下生成一個名為 `exchange-program_NTUST.xlsx` 的Excel檔，其中包含整合後的交換學校資訊。

### 注意事項

- 請確保已安裝所需的套件。
- 程式執行過程中可能會因為網站結構變更而失效，建議定期檢查更新。

### 免責聲明

此程式僅供學術研究和個人使用，使用者須自行承擔相關風險。開發者不對程式使用所產生的任何損失或損害負責。

# README (English Version)

## Exchange School Information Integration Program

### Introduction

This program is designed to integrate the list of exchange schools for the National Taiwan University of Science and Technology (NTUST) in the 112-2 semester (Spring 2024) with the QS rankings of those schools. The results are then output to an Excel file. The program uses web scraping to gather the required information from the NTUST website and the QS ranking website.

### Usage

1. Install dependencies:

   ```bash
   pip install pandas requests beautifulsoup4
   ```

2. Run the program:

   ```bash
   python exchange-program_NTUST.py
   ```

3. Check the output:

   After the program completes execution, an Excel file named `exchange-program_NTUST.xlsx` will be generated in the same directory, containing the integrated exchange school information.

### Notes

- Make sure to install the required packages.
- The program may become obsolete due to changes in the website structure; periodic checks for updates are recommended.

### Disclaimer

This program is for academic research and personal use only. Users are responsible for any risks associated with its usage. The developer is not liable for any losses or damages resulting from the use of the program.
