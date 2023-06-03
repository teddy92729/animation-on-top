# animation-on-top

需先安裝python

初次使用先執行venv.bat，安裝虛擬環境和依賴項

創建動畫方式:

  創建資料夾，並複製conf.py和動畫(須拆分成圖像)
  
    start.bat
    venv.bat
    main.py
    |--dir
      |--conf.py
      |--0.png
      |--1.png
      |--...
      
 conf.py需設定圖像的格式
 
圖像位移量

    offset=(0,0)  
  
圖像顯示大小

    size=(100,100)

假設動畫有9張，檔名為0.png,1.png,...,9.png
  
第一幀索引

    startFrameIndex=0
  
最後一幀索引

    endFrameIndex=9
  
設定圖像名稱格式

    filenameFormat="%d.png"
  
幀數

    fps=30
  
選擇透明化的顏色

    # transparent=None 

    transparent=(255,255,255) 
  

 使用方式: 
 
 將資料夾拖移到start.bat
 
  
