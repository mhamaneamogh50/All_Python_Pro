import instaloader
mod=instaloader.Instaloader
a=input("Enter the profile name --> ")
mod.download_profile(a,profile_pic_only=True)
