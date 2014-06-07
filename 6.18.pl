#!/usr/bin/perl

use strict;
use warnings;

package MyEncoding;

sub new {
    return bless {} => shift;
}

sub encode {
    my ($self, $str) = @_;
    my @str = split(//, $str);
    my ($prev, $count, $encoded) = ($str[0], 1, '');

    for (my $j = 1; $j < scalar(@str); $j++) {
#        warn "j $j str $str[$j]";
        if ($str[$j] ne $prev) {
            $encoded .= "$count$prev";
            $count = 0;
        }
        $count++;
        $prev = $str[$j];
    }
    $encoded .= $prev ? "$count$prev" : '';
    return $encoded;
}

sub decode {
    my ($self, $str) = @_;
    my @str = split(//, $str);
    my ($letter, $count, $decoded) = ('', 0, '');

    for (my $j = 0; $j < scalar(@str); $j += 1) {
        if ($str[$j] =~ /\d/) { # count
            $count .= $str[$j];
        }
        else { # letter
            $letter = $str[$j];
            $decoded .= $letter x $count;
            $count = '';
        }
    }

    return $decoded;
}

package TestMyEncoding;
use Test::More;
use Test::Deep;

my $module = MyEncoding->new;
is($module->encode(''), '', 'empty str OK');
is($module->encode('a'), '1a', 'a OK');
is($module->encode('aaa'), '3a', 'aaa OK');
is($module->encode('aacccb'), '2a3c1b', 'aaccb OK');
is($module->encode('aaaacbbb'), '4a1c3b', 'aaaacbbb OK');
is($module->decode(''), '', 'decode: empty str OK');
is($module->decode('1a'), 'a', 'decode: 1a OK');
is($module->decode('2a'), 'aa', 'decode: 2a OK');
is($module->decode('3a1c2b6d'), 'aaacbbdddddd', 'decode: 3a1c2b6d OK');
is($module->decode('1a2b1a'), 'abba', 'decode: 1a2b1a OK');
is($module->decode('11z'), 'zzzzzzzzzzz', 'decode: 2a OK');


done_testing;
