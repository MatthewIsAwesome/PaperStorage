   M S B A M L   `   `   `  ����?  ;Main, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:MainMain  5   	       Main.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   $localclr-namespace:Main     5   	     � Title$  Paper Storage��5   	   $��359.428��6   $	��300��60   .��5	      ��  �� Padding$ 5q�6   $��1q�6   ._�5
   
   �� .+�5      �� $
��Wrap=�6   $��12(�6,   $k��eThis is the GUI for Paper Storage select from the options below to store files in the form of images.��6:   �� 5      $
��Wrap=�6   $��15(�6-    �� Padding$ 0 10 0 0q�6;   $��Input Path:��6N   � 5       � ColumnDefinitions 5      �� 5      $
��.94* �6'   �� 5      $
��.07* �6'   .+�5      �� -   5         ��Name$ InputBox��5   '   $��0��6   6'   �� 5      -   5         ��Name$ InputButton��5   )   $��1��6   $��···��6>   6L   5      �� 5      $
��Wrap=�6   $��15(�6,   $ 0 10 0 0q�6:   $��Output Path:��6M   � 5       5      �� 5      $
��.94* �6'   �� 5      $
��.07* �6'   .+�5      �� -   5        $��	OutputBox��5   ,   $��0 0 0 15q�6   $��0��6=   �� 5      -   5        $ OutputButton��5   )   $��1��6   $��···��6?   $	��Top=�6M   $��0,0,0,15q�6e   6w   5      �� 5!      -   5         ��Name$ AdvancedEnable��5!      $��Advanced Options��6u   �� 5#      $
��Wrap=�6   $��15(�6,   $ 0 1 0 0q�6:   $��Height:��6L   �� 5$      -   5        $ 	HeightBox��5$      {�.  $
��1000��6;   �� 5%      $
��Wrap=�6   $��15(�6,   $ 0 10 0 0q�6:   $��Width:��6M   �� 5&      -   5        $ WidthBox��5&      {�.  $
��1000��6:   � 5(       5)      �� 5*      $��* �6'   �� 5+      $��* �6'   .+�5-      �� -   5        $ Reset��5-      $��0��6<   $��Reset��6L   $��0 10 5 0q�6\   �� 5.      -	   5        $ Start��5.      $��1��6<   $��Start��6L   $��5 10 0 0q�6\   5/      �� 50      $��0 10 0 0q�6   ���#D0D1D4$��1q�6=   ._�51      �� -
   5         ��Name$ Output��51   �   ���#D0D1D4$ 2 2 0 3q�61   $
��Wrap=�6C   $��Center=�6W   $��Output��6r   6�   52      53      54      55      