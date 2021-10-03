File.open("fcdir.txt", "r") do |f|
    f.each_line do |line|
      $dir = line
      puts line
    end
  end
Dir.chdir(Dir.home)
Dir.chdir($dir)
puts system("pwd")