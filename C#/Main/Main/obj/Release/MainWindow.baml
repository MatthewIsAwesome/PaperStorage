   M S B A M L   `   `   `  ���� ?  ;Main, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:MainMain      Main.MainWindow   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     @d2http://schemas.microsoft.com/expression/blend/2008     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     $localclr-namespace:Main       � Title$  Paper Storage��$	��370��$	��300��.����  �� Padding$ 5q�$��1q�._��� .+��� $
��Wrap=�$��12(�$k��eThis is the GUI for Paper Storage select from the options below to store files in the form of images.���� $
��Wrap=�$��15(� �� Padding$ 0 10 0 0q�$��Input Path:���  � ColumnDefinitions �� $
��.94* ��� $
��.07* �.+��� -    ��Name$ InputBox��$��0���� -    ��Name$ InputButton��$��1��$��···���� $
��Wrap=�$��15(�$ 0 10 0 0q�$��Output Path:���  �� $
��.94* ��� $
��.07* �.+��� -   $��	OutputBox��$��0 0 0 15q�$��0���� -   $ OutputButton��$��1��$��···��$	��Top=�$��0,0,0,15q��� -    ��Name$ AdvancedEnable��$��Advanced Options���� $
��Wrap=�$��15(�$ 0 1 0 0q�$��Height:���� -   $ 	HeightBox��{�.  $
��1000���� $
��Wrap=�$��15(�$ 0 10 0 0q�$��Width:���� -   $ WidthBox��{�.  $
��1000���  �� $��* ��� $��* �.+��� -   $ Reset��$��0��$��Reset��$��0 10 5 0q��� -	   $ Start��$��1��$��Start��$��5 10 0 0q��� $��0 10 0 0q����#D0D1D4$��1q�._��� -
    ��Name$ Output�����#D0D1D4$ 2 2 0 3q�$
��Wrap=�$��Center=�$��Output��