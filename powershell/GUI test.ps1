<# This form was created using POSHGUI.com  a free online gui designer for PowerShell
.NAME
    Paper Storage
#>

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$Window                          = New-Object system.Windows.Forms.Form
$Window.ClientSize               = '583,592'
$Window.text                     = "Paper Storage GUI"
$Window.TopMost                  = $false

$TextBox1                        = New-Object system.Windows.Forms.TextBox
$TextBox1.multiline              = $false
$TextBox1.text                   = "Input Path"
$TextBox1.width                  = 551
$TextBox1.height                 = 44
$TextBox1.location               = New-Object System.Drawing.Point(14,35)
$TextBox1.Font                   = 'Microsoft Sans Serif,10'

$Window.controls.AddRange(@($TextBox1))

$Window.ShowDialog()