
$once = 1

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Application]::EnableVisualStyles()

$Window                          = New-Object system.Windows.Forms.Form
$Window.ClientSize               = '385,201'
$Window.text                     = "Paper Storage GUI"
$Window.BackColor                = "#ffffff"
$Window.TopMost                  = $false

$Testtip                         = New-Object system.Windows.Forms.ToolTip
$Testtip.ToolTipTitle            = "Put the path to the folder you want to paperback"
$Testtip.isBalloon               = $true

$EncodeButton                    = New-Object system.Windows.Forms.Button
$EncodeButton.BackColor          = "#4a90e2"
$EncodeButton.text               = "Encode"
$EncodeButton.width              = 111
$EncodeButton.height             = 78
$EncodeButton.location           = New-Object System.Drawing.Point(47,62)
$EncodeButton.Font               = 'Microsoft Sans Serif,10'

$DecodeButton                    = New-Object system.Windows.Forms.Button
$DecodeButton.BackColor          = "#4a90e2"
$DecodeButton.text               = "Decode"
$DecodeButton.width              = 110
$DecodeButton.height             = 78
$DecodeButton.location           = New-Object System.Drawing.Point(216,61)
$DecodeButton.Font               = 'Microsoft Sans Serif,10'

$Window.controls.AddRange(@($EncodeButton,$DecodeButton))





While($true){
    $EncodeButton.Add_Click({$encodeclick = 1 })
    $DecodeButton.Add_Click({$decodeclick = 1; echo 'test'})
    
    if($encodeclick -eq 1){echo 'encode clicked'
        $encodeclick = 0
        
        }

    if($decodeclick -eq 1){
        $decodeclick = 0
        }       
    if($once -eq 1){
        $Window.ShowDialog()
        $once = 0
        }
    
    
    
    
    }


