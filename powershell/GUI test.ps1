Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$Window                          = New-Object system.Windows.Forms.Form
$Window.ClientSize               = '583,544'
$Window.text                     = "Paper Storage GUI"
$Window.BackColor                = "#ffffff"
$Window.TopMost                  = $false

$TextBox1                        = New-Object system.Windows.Forms.TextBox
$TextBox1.multiline              = $false
$TextBox1.text                   = "Input Path"
$TextBox1.width                  = 551
$TextBox1.height                 = 44
$TextBox1.location               = New-Object System.Drawing.Point(14,35)
$TextBox1.Font                   = 'Microsoft Sans Serif,10'

$Testtip                         = New-Object system.Windows.Forms.ToolTip
$Testtip.ToolTipTitle            = "Put the path to the folder you want to paperback"
$Testtip.isBalloon               = $true

$ComboBoxEncodeDecode            = New-Object system.Windows.Forms.ComboBox
$ComboBoxEncodeDecode.text       = "Encode"
$ComboBoxEncodeDecode.DropDownStyle = 'DropDownList'
$ComboBoxEncodeDecode.Items.Add('Encode')
$ComboBoxEncodeDecode.Items.Add('Decode')
$ComboBoxEncodeDecode.width      = 100
$ComboBoxEncodeDecode.height     = 20
$ComboBoxEncodeDecode.location   = New-Object System.Drawing.Point(142,171)
$ComboBoxEncodeDecode.Font       = 'Microsoft Sans Serif,10'

$Window.controls.AddRange(@($TextBox1,$ComboBoxEncodeDecode))

$Window.Add_BackColorChanged({  })


$Window.ShowDialog()